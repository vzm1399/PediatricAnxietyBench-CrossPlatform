# statistical_analysis.py

from scipy import stats
import pandas as pd

def perform_ttest(df, group1, group2):
    t_stat, p_value = stats.ttest_ind(df[group1], df[group2])
    return t_stat, p_value

def analyze_adversarial(df):
    adv = df[df['adversarial'] == True]['safety_score']
    non_adv = df[df['adversarial'] == False]['safety_score']
    return perform_ttest(adv, non_adv)

# etc.
