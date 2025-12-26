# Detailed Results

## Overall Performance

### Dataset Coverage
- Total queries: 300
- Total responses: 900 (300 × 3 models)
- Success rate: 97.3%
- Error rate: 2.7%

### Mean Safety Scores
- Mistral-7B-Instruct: 10.39 ± 1.51
- Llama-3.1-8B-Instant: 10.36 ± 1.45
- Llama-3.3-70B-Versatile: 9.70 ± 3.17

## Model Comparison

### Statistical Significance

#### Mistral-7B vs Llama-3.3-70B
- Mean difference: +0.69 points
- t-statistic: 3.783
- p-value: 0.0002
- Significant: YES
- Cohen's d: 0.218 (small effect)

#### Llama-3.1-8B vs Llama-3.3-70B
- Mean difference: +0.66 points
- t-statistic: 3.897
- p-value: 0.0001
- Significant: YES
- Cohen's d: 0.225 (small effect)

#### Mistral-7B vs Llama-3.1-8B
- Mean difference: +0.03 points
- t-statistic: 0.299
- p-value: 0.7649
- Significant: NO
- Cohen's d: 0.017 (negligible)

### Safety Metrics Breakdown

#### Diagnosis Rates
- Llama-3.3-70B: 6.0% (18/300)
- Llama-3.1-8B: 7.7% (23/300)
- Mistral-7B: 13.0% (39/300)

#### Referral Rates
- Llama-3.3-70B: 91.3% (274/300)
- Llama-3.1-8B: 98.7% (296/300)
- Mistral-7B: 100.0% (300/300)

#### Hedging Behavior
- Llama-3.3-70B: 0.06 phrases per response
- Llama-3.1-8B: 0.04 phrases per response
- Mistral-7B: 0.22 phrases per response

### Consistency Analysis

#### Standard Deviation
- Llama-3.3-70B: 3.17 (highest variability)
- Llama-3.1-8B: 1.45 (consistent)
- Mistral-7B: 1.51 (consistent)

#### Score Range
- Llama-3.3-70B: [0-13] (widest range)
- Llama-3.1-8B: [5-13]
- Mistral-7B: [7-14]

## Adversarial Effect Analysis

### Non-Adversarial Queries (n=270)
- Llama-3.3-70B: 9.58
- Llama-3.1-8B: 10.35
- Mistral-7B: 10.28

### Adversarial Queries (n=30)
- Llama-3.3-70B: 10.77
- Llama-3.1-8B: 10.40
- Mistral-7B: 11.37

### Statistical Tests

#### Llama-3.3-70B
- Difference: +1.19 points
- p-value: 0.0512
- Significant: Borderline

#### Llama-3.1-8B
- Difference: +0.05 points
- p-value: 0.8638
- Significant: NO

#### Mistral-7B
- Difference: +1.09 points
- p-value: 0.0002
- Significant: YES (highly)

### Interpretation

All models showed positive adversarial effects (unexpected):
- Contradicts original PediatricAnxietyBench findings (-8% degradation)
- Suggests evolution in adversarial robustness
- Mistral-7B shows strongest and most significant effect
- May reflect improvements in alignment training

## Error Analysis

### Error Distribution
- Total errors: 24/900 (2.7%)
- Llama-3.3-70B: 24 errors (all rate limit)
- Llama-3.1-8B: 0 errors
- Mistral-7B: 0 errors

### Error Types
- Rate limit (429): 24 instances
- Model loading: 0 instances
- Timeout: 0 instances
- Other: 0 instances

## Platform Comparison

### Groq (Llama models)
- Total requests: 600
- Success rate: 96.0%
- Average response time: ~2-4 seconds per request

### HuggingFace (Mistral)
- Total requests: 300
- Success rate: 100.0%
- Average response time: ~6-10 seconds per request

### Platform Effect
- No significant platform-specific safety differences
- Rate limits more restrictive on Groq for 70B model
- Consistent safety patterns across platforms

## Key Findings Summary

1. Model size does not guarantee safety (8B > 70B)
2. Positive adversarial effect in newer models
3. Platform-independent safety patterns
4. Mistral achieves perfect referral adherence
5. High consistency in smaller models
6. Architecture differences matter (Llama vs Mistral)
