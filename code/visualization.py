# Cell: Comprehensive Visualizations - 300 queries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.4)

df = pd.read_csv('evaluated_results_300.csv')

fig = plt.figure(figsize=(18, 12))
colors = ['#2E86AB', '#A23B72', '#F18F01']
model_names = ['Llama-3.3-70B', 'Llama-3.1-8B', 'Mistral-7B']

# 1. Safety Scores Bar Chart
ax1 = plt.subplot(2, 3, 1)
means = [
    df['Llama-3.3-70B-Versatile_safety_score'].mean(),
    df['Llama-3.1-8B-Instant_safety_score'].mean(),
    df['Mistral-7B-Instruct_safety_score'].mean()
]
stds = [
    df['Llama-3.3-70B-Versatile_safety_score'].std(),
    df['Llama-3.1-8B-Instant_safety_score'].std(),
    df['Mistral-7B-Instruct_safety_score'].std()
]

bars = ax1.bar(range(3), means, yerr=stds, capsize=8,
               color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
ax1.set_xticks(range(3))
ax1.set_xticklabels(model_names, rotation=20, ha='right')
ax1.set_ylabel('Mean Safety Score', fontweight='bold')
ax1.set_title('(A) Safety Score by Model (n=300)', fontweight='bold')
ax1.set_ylim([0, 15])
ax1.axhline(y=10, color='gray', linestyle='--', alpha=0.5)

for bar, mean, std in zip(bars, means, stds):
    ax1.text(bar.get_x() + bar.get_width()/2, mean + std + 0.5,
             f'{mean:.2f}', ha='center', fontweight='bold', fontsize=12)

# 2. Diagnosis Rate
ax2 = plt.subplot(2, 3, 2)
diag_rates = [
    (df['Llama-3.3-70B-Versatile_has_diagnosis'].sum() / len(df)) * 100,
    (df['Llama-3.1-8B-Instant_has_diagnosis'].sum() / len(df)) * 100,
    (df['Mistral-7B-Instruct_has_diagnosis'].sum() / len(df)) * 100
]

bars = ax2.bar(range(3), diag_rates, color=colors, alpha=0.8,
               edgecolor='black', linewidth=1.5)
ax2.set_xticks(range(3))
ax2.set_xticklabels(model_names, rotation=20, ha='right')
ax2.set_ylabel('Diagnosis Rate (%)', fontweight='bold')
ax2.set_title('(B) Inappropriate Diagnosis Rate', fontweight='bold')

for bar, rate in zip(bars, diag_rates):
    ax2.text(bar.get_x() + bar.get_width()/2, rate + 0.5,
             f'{rate:.1f}%', ha='center', fontweight='bold')

# 3. Referral Rate
ax3 = plt.subplot(2, 3, 3)
ref_rates = [
    (df['Llama-3.3-70B-Versatile_has_referral'].sum() / len(df)) * 100,
    (df['Llama-3.1-8B-Instant_has_referral'].sum() / len(df)) * 100,
    (df['Mistral-7B-Instruct_has_referral'].sum() / len(df)) * 100
]

bars = ax3.bar(range(3), ref_rates, color=colors, alpha=0.8,
               edgecolor='black', linewidth=1.5)
ax3.set_xticks(range(3))
ax3.set_xticklabels(model_names, rotation=20, ha='right')
ax3.set_ylabel('Referral Rate (%)', fontweight='bold')
ax3.set_title('(C) Professional Referral Rate', fontweight='bold')
ax3.set_ylim([85, 100])

for bar, rate in zip(bars, ref_rates):
    ax3.text(bar.get_x() + bar.get_width()/2, rate - 2,
             f'{rate:.1f}%', ha='center', fontweight='bold', color='white', fontsize=11)

# 4. Distribution Histogram
ax4 = plt.subplot(2, 3, 4)
for i, (col, color, name) in enumerate(zip(
    ['Llama-3.3-70B-Versatile_safety_score',
     'Llama-3.1-8B-Instant_safety_score',
     'Mistral-7B-Instruct_safety_score'],
    colors, model_names
)):
    ax4.hist(df[col], bins=range(0, 16), alpha=0.6,
             label=name, color=color, edgecolor='black', linewidth=0.8)

ax4.set_xlabel('Safety Score', fontweight='bold')
ax4.set_ylabel('Frequency', fontweight='bold')
ax4.set_title('(D) Safety Score Distribution', fontweight='bold')
ax4.legend(loc='upper left')
ax4.set_xlim([0, 15])

# 5. Adversarial vs Non-Adversarial ⭐
ax5 = plt.subplot(2, 3, 5)

adv = df[df['adversarial'] == True]
non_adv = df[df['adversarial'] == False]

x = np.arange(3)
width = 0.35

non_adv_means = [
    non_adv['Llama-3.3-70B-Versatile_safety_score'].mean(),
    non_adv['Llama-3.1-8B-Instant_safety_score'].mean(),
    non_adv['Mistral-7B-Instruct_safety_score'].mean()
]

adv_means = [
    adv['Llama-3.3-70B-Versatile_safety_score'].mean(),
    adv['Llama-3.1-8B-Instant_safety_score'].mean(),
    adv['Mistral-7B-Instruct_safety_score'].mean()
]

bars1 = ax5.bar(x - width/2, non_adv_means, width, label='Non-Adversarial (n=270)',
                color='#6C8EBF', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax5.bar(x + width/2, adv_means, width, label='Adversarial (n=30)',
                color='#D79B00', alpha=0.8, edgecolor='black', linewidth=1.5)

ax5.set_ylabel('Mean Safety Score', fontweight='bold')
ax5.set_title('(E) Adversarial Effect ⭐', fontweight='bold')
ax5.set_xticks(x)
ax5.set_xticklabels(model_names, rotation=20, ha='right')
ax5.legend()
ax5.set_ylim([8, 13])

# Add significance stars for Mistral
ax5.text(2, adv_means[2] + 0.3, '***', ha='center', fontsize=16, fontweight='bold')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height + 0.15,
                f'{height:.2f}', ha='center', fontsize=9, fontweight='bold')

# 6. Box Plot
ax6 = plt.subplot(2, 3, 6)

data_box = [
    df['Llama-3.3-70B-Versatile_safety_score'],
    df['Llama-3.1-8B-Instant_safety_score'],
    df['Mistral-7B-Instruct_safety_score']
]

bp = ax6.boxplot(data_box, tick_labels=model_names, patch_artist=True,
                 showmeans=True, meanline=True)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax6.set_ylabel('Safety Score', fontweight='bold')
ax6.set_title('(F) Score Distribution (Box Plot)', fontweight='bold')
ax6.set_xticklabels(model_names, rotation=20, ha='right')
ax6.set_ylim([0, 15])
ax6.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/content/drive/MyDrive/LLM_Evaluation/comprehensive_figure_300.png', 
            dpi=300, bbox_inches='tight')

print("✅ Figure saved: comprehensive_figure_300.png")
plt.show()
