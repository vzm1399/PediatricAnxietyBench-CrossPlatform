# Cell: Statistical Analysis - 300 queries
from scipy import stats
import numpy as np

print("="*60)
print("STATISTICAL ANALYSIS - 300 QUERIES")
print("="*60)

df = pd.read_csv('evaluated_results_300.csv')

scores = {
    'Llama-3.3-70B': df['Llama-3.3-70B-Versatile_safety_score'],
    'Llama-3.1-8B': df['Llama-3.1-8B-Instant_safety_score'],
    'Mistral-7B': df['Mistral-7B-Instruct_safety_score']
}

# Descriptive stats
print("\n📊 Descriptive Statistics:")
print("-"*60)
for name, score in scores.items():
    print(f"\n{name}:")
    print(f"  Mean: {score.mean():.2f}")
    print(f"  SD: {score.std():.2f}")
    print(f"  Median: {score.median():.0f}")
    print(f"  Min-Max: [{score.min()}, {score.max()}]")

# Paired t-tests
print("\n" + "="*60)
print("📈 PAIRED T-TESTS")
print("="*60)

comparisons = [
    ('Mistral-7B vs Llama-3.3-70B', scores['Mistral-7B'], scores['Llama-3.3-70B']),
    ('Llama-3.1-8B vs Llama-3.3-70B', scores['Llama-3.1-8B'], scores['Llama-3.3-70B']),
    ('Mistral-7B vs Llama-3.1-8B', scores['Mistral-7B'], scores['Llama-3.1-8B'])
]

stats_results = []

for comp_name, score_a, score_b in comparisons:
    t_stat, p_val = stats.ttest_rel(score_a, score_b)
    diff = score_a - score_b
    cohens_d = diff.mean() / diff.std()
    
    if abs(cohens_d) < 0.2:
        effect = "negligible"
    elif abs(cohens_d) < 0.5:
        effect = "small"
    elif abs(cohens_d) < 0.8:
        effect = "medium"
    else:
        effect = "large"
    
    print(f"\n{comp_name}:")
    print(f"  Mean difference: {score_a.mean() - score_b.mean():.2f}")
    print(f"  t-statistic: {t_stat:.3f}")
    print(f"  p-value: {p_val:.4f}")
    print(f"  Significant (p<0.05)? {'YES ✅' if p_val < 0.05 else 'NO'}")
    print(f"  Cohen's d: {cohens_d:.3f}")
    print(f"  Effect size: {effect}")
    
    stats_results.append({
        'comparison': comp_name,
        't_statistic': t_stat,
        'p_value': p_val,
        'cohens_d': cohens_d,
        'effect_size': effect,
        'mean_diff': score_a.mean() - score_b.mean()
    })

# Save stats
pd.DataFrame(stats_results).to_csv('statistical_tests_300.csv', index=False)

# Adversarial analysis
print("\n" + "="*60)
print("🎭 ADVERSARIAL vs NON-ADVERSARIAL")
print("="*60)

adv = df[df['adversarial'] == True]
non_adv = df[df['adversarial'] == False]

print(f"\nNon-Adversarial (n={len(non_adv)}):")
for name, col in [('Llama-3.3-70B', 'Llama-3.3-70B-Versatile_safety_score'),
                   ('Llama-3.1-8B', 'Llama-3.1-8B-Instant_safety_score'),
                   ('Mistral-7B', 'Mistral-7B-Instruct_safety_score')]:
    print(f"  {name}: {non_adv[col].mean():.2f}")

print(f"\nAdversarial (n={len(adv)}):")
for name, col in [('Llama-3.3-70B', 'Llama-3.3-70B-Versatile_safety_score'),
                   ('Llama-3.1-8B', 'Llama-3.1-8B-Instant_safety_score'),
                   ('Mistral-7B', 'Mistral-7B-Instruct_safety_score')]:
    print(f"  {name}: {adv[col].mean():.2f}")
    
# Adversarial effect
print("\n" + "-"*60)
print("Adversarial Effect Analysis:")

for name, col in [('Llama-3.3-70B', 'Llama-3.3-70B-Versatile_safety_score'),
                   ('Llama-3.1-8B', 'Llama-3.1-8B-Instant_safety_score'),
                   ('Mistral-7B', 'Mistral-7B-Instruct_safety_score')]:
    
    t_adv, p_adv = stats.ttest_ind(non_adv[col], adv[col])
    diff = non_adv[col].mean() - adv[col].mean()
    
    print(f"\n{name}:")
    print(f"  Difference: {diff:.2f} points")
    print(f"  p-value: {p_adv:.4f}")
    print(f"  Significant? {'YES ✅' if p_adv < 0.05 else 'NO'}")

# Save adversarial breakdown
adv_breakdown = []
for name, col in [('Llama-3.3-70B-Versatile', 'Llama-3.3-70B-Versatile_safety_score'),
                   ('Llama-3.1-8B-Instant', 'Llama-3.1-8B-Instant_safety_score'),
                   ('Mistral-7B-Instruct', 'Mistral-7B-Instruct_safety_score')]:
    adv_breakdown.append({
        'Model': name,
        'Non_Adversarial_n': len(non_adv),
        'Non_Adversarial_mean': non_adv[col].mean(),
        'Adversarial_n': len(adv),
        'Adversarial_mean': adv[col].mean(),
        'Difference': adv[col].mean() - non_adv[col].mean()
    })

pd.DataFrame(adv_breakdown).to_csv('adversarial_breakdown_300.csv', index=False)

print("\n" + "="*60)
print("✅ STATISTICAL ANALYSIS COMPLETE")
print("="*60)
print("Files saved:")
print("  - statistical_tests_300.csv")
print("  - adversarial_breakdown_300.csv")
