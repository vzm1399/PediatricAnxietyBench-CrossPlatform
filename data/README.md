# Dataset

## Overview

The PediatricAnxietyBench dataset consists of 300 pediatric health queries designed to test LLM safety under parental anxiety and pressure.

## Structure

- **Total**: 300 queries
- **Non-adversarial**: 270 (90%)
- **Adversarial**: 30 (10%)

## Topics

| Topic | Count | Percentage |
|-------|-------|------------|
| Fever | 50 | 16.7% |
| Respiratory | 27 | 9.0% |
| Head injury | 24 | 8.0% |
| Vomiting/diarrhea | 20 | 6.7% |
| Skin rash | 21 | 7.0% |
| Other | 158 | 52.6% |

## Access

- **Sample**: 20 queries included in `sample_queries.jsonl`
- **Full dataset**: Available via [original repository](https://github.com/vzm1399/PediatricAnxietyBench)
- **Format**: JSONL with fields: `id`, `text`, `topic`, `adversarial`, `source`

## Citation

See main [README](../README.md) for citation information.
