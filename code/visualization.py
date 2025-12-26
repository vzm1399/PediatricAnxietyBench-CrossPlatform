# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_safety_scores(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='model', y='safety_score', hue='adversarial')
    plt.savefig('safety_scores.png')

# Comprehensive figure from the notebook
# paste code for creating comprehensive_figure_300.png
