# Evaluation Summary Report

**Date:** December 26, 2025  
**Dataset:** 300 queries (150 adversarial, 150 non-adversarial)  
**Models Evaluated:** Gemini 1.5 Flash, Llama 3.1 70B, Mistral 8x7B  
**Platforms:** Google AI Studio, Groq  

---

## Key Findings

### Overall Safety Scores (mean ± std)
- **Gemini 1.5 Flash** (Google): 3.45 ± 1.2
- **Llama 3.1 70B** (Groq): 2.89 ± 1.4
- **Mistral 8x7B** (Groq): 4.12 ± 0.9

### Adversarial Impact
- **Mistral**: Significantly higher safety on adversarial queries (4.5 vs 3.7, *p* < 0.001)
- **Llama**: Lower safety on adversarial queries (2.5 vs 3.2, *p* = 0.002)
- **Gemini**: No significant difference (*p* = 0.15)

### Platform Comparison
- Performance of Gemini models on Google vs Groq: Similar (*p* = 0.42)
- Model size paradox: Smaller model (8B) outperformed larger model (70B) in safety

### Topic Breakdown
- Highest safety score: **Vaccination** (4.2)
- Lowest safety score: **Mental health** (2.8)

### Other Insights
- Disclaimer usage present in 85% of safe responses
- Strong awareness of medical terminology across models
- Diagnosis restraint varies significantly by model
- Hedging behavior strongly correlates with higher safety scores

**End of Report**
