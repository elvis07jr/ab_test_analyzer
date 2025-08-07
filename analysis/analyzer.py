import pandas as pd
from scipy.stats import ttest_ind

def analyze_conversion_rate(df: pd.DataFrame):
    """
    Analyzes the conversion rate between two groups.
    """
    a_conv = df[df['group'] == 'A']['converted']
    b_conv = df[df['group'] == 'B']['converted']

    stat, p_value = ttest_ind(a_conv, b_conv)

    return stat, p_value

def analyze_average_spend(df: pd.DataFrame):
    """
    Analyzes the average spend between two groups.
    """
    a_spend = df[(df['group'] == 'A') & (df['converted'])]['revenue']
    b_spend = df[(df['group'] == 'B') & (df['converted'])]['revenue']

    stat, p_value = ttest_ind(a_spend, b_spend)

    return stat, p_value

def analyze_bounce_rate(df: pd.DataFrame):
    """
    Analyzes the bounce rate between two groups.
    """
    a_bounce = df[df['group'] == 'A']['bounced']
    b_bounce = df[df['group'] == 'B']['bounced']

    stat, p_value = ttest_ind(a_bounce, b_bounce)

    return stat, p_value
