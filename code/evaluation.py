# Cell: COMPLETE EVALUATION - Setup + Functions + Run
import pandas as pd
from tqdm import tqdm
from datetime import datetime
import time
from groq import Groq
from huggingface_hub import InferenceClient
from google.colab import userdata

# ==========================================
# STEP 1: SETUP APIs
# ==========================================
print("STEP 1: Setting up APIs...")
GROQ_API_KEY = userdata.get('grokapikey')
HF_TOKEN = userdata.get('huggingfaceapikey')

groq_client = Groq(api_key=GROQ_API_KEY)
hf_client = InferenceClient(token=HF_TOKEN)
print("✅ APIs ready\n")

# ==========================================
# STEP 2: DEFINE FUNCTIONS
# ==========================================
print("STEP 2: Defining response functions...")

def get_groq_response(query, model_name, max_retries=3):
    for attempt in range(max_retries):
        try:
            completion = groq_client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": query}],
                temperature=0.7,
                max_tokens=500
            )
            return completion.choices[0].message.content
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep((attempt + 1) * 5)
            else:
                return f"ERROR: {str(e)}"
    return "ERROR: Max retries"

def get_hf_response(query, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = hf_client.chat_completion(
                model="mistralai/Mistral-7B-Instruct-v0.2",
                messages=[{"role": "user", "content": query}],
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            if 'loading' in str(e).lower():
                time.sleep(30)
            elif attempt < max_retries - 1:
                time.sleep((attempt + 1) * 10)
            else:
                return f"ERROR: {str(e)}"
    return "ERROR: Max retries"

print("✅ Functions ready\n")

# ==========================================
# STEP 3: FULL EVALUATION
# ==========================================
print("="*70)
print("STEP 3: FULL EVALUATION - 300 QUERIES")
print("="*70)

print(f"\nDataset: {len(df_full)} queries")
print(f"  Non-adversarial: {(df_full['adversarial']==False).sum()}")
print(f"  Adversarial: {(df_full['adversarial']==True).sum()}")

models_config = {
    'Llama-3.3-70B-Versatile': {
        'function': lambda q: get_groq_response(q, 'llama-3.3-70b-versatile'),
        'delay': 2
    },
    'Llama-3.1-8B-Instant': {
        'function': lambda q: get_groq_response(q, 'llama-3.1-8b-instant'),
        'delay': 2
    },
    'Mistral-7B-Instruct': {
        'function': lambda q: get_hf_response(q),
        'delay': 6
    }
}

print(f"\nTotal requests: 900")
print(f"Estimated time: ~50 minutes")
print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
print("="*70 + "\n")

results = []
start_time = time.time()

for idx, row in tqdm(df_full.iterrows(), total=len(df_full), desc="Progress"):
    query = row['query']
    
    result_row = {
        'query_id': row['id'],
        'query': query,
        'topic': row['topic'],
        'adversarial': row['adversarial'],
        'source': row['source']
    }
    
    for model_name, config in models_config.items():
        try:
            response = config['function'](query)
            result_row[f'{model_name}_response'] = response
        except Exception as e:
            result_row[f'{model_name}_response'] = f"ERROR: {e}"
        
        time.sleep(config['delay'])
    
    results.append(result_row)
    
    if (idx + 1) % 50 == 0:
        pd.DataFrame(results).to_csv('checkpoint_300.csv', index=False)
        elapsed = time.time() - start_time
        remaining = (elapsed / (idx + 1)) * (len(df_full) - idx - 1)
        print(f"\n💾 {idx+1}/300 | {elapsed/60:.1f}min | ~{remaining/60:.1f}min left")

df_results_full = pd.DataFrame(results)
df_results_full.to_csv('full_results_300.csv', index=False)

print(f"\n✅ DONE! Time: {(time.time()-start_time)/60:.1f} min")
print(f"Saved: full_results_300.csv")

error_count = sum(1 for col in df_results_full.columns if 'response' in col
                  for val in df_results_full[col] if 'ERROR' in str(val))
print(f"Errors: {error_count}/900")
