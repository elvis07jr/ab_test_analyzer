import streamlit as st
import pandas as pd
import duckdb
import sys
import os
import altair as alt

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analysis.analyzer import analyze_conversion_rate, analyze_average_spend, analyze_bounce_rate

st.title("A/B Test Analyzer")

st.markdown("""
This application analyzes A/B test data from a CSV file.
Please upload your data to see the results.
""")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data", data.head())

    # --- SQL Analysis ---
    st.write("### A/B Test Metrics")
    with open("../sql/queries.sql", "r") as f:
        sql_query = f.read()

    # Create an in-memory DuckDB database
    con = duckdb.connect(database=':memory:', read_only=False)
    # Register the DataFrame as a table
    con.register('users', data)
    # Execute the query
    results_df = con.execute(sql_query).fetchdf()
    con.close()

    st.write(results_df)

    # --- Statistical Analysis ---
    st.write("### Statistical Significance (p-values)")

    # Conversion Rate
    cr_stat, cr_p_value = analyze_conversion_rate(data)
    st.write(f"**Conversion Rate:** p-value = {cr_p_value:.4f}")
    if cr_p_value < 0.05:
        st.success("The difference in conversion rate is statistically significant.")
    else:
        st.warning("The difference in conversion rate is not statistically significant.")

    # Average Spend
    as_stat, as_p_value = analyze_average_spend(data)
    st.write(f"**Average Spend:** p-value = {as_p_value:.4f}")
    if as_p_value < 0.05:
        st.success("The difference in average spend is statistically significant.")
    else:
        st.warning("The difference in average spend is not statistically significant.")

    # Bounce Rate
    br_stat, br_p_value = analyze_bounce_rate(data)
    st.write(f"**Bounce Rate:** p-value = {br_p_value:.4f}")
    if br_p_value < 0.05:
        st.success("The difference in bounce rate is statistically significant.")
    else:
        st.warning("The difference in bounce rate is not statistically significant.")

    # --- Charts ---
    st.write("### Visualizations")

    # Conversion Rate Chart
    conv_chart = alt.Chart(results_df).mark_bar().encode(
        x='group:N',
        y='conversion_rate:Q',
        color='group:N',
        tooltip=['group', 'conversion_rate']
    ).properties(
        title='Conversion Rate by Group'
    )
    st.altair_chart(conv_chart, use_container_width=True)

    # Average Spend Chart
    avg_spend_chart = alt.Chart(results_df).mark_bar().encode(
        x='group:N',
        y='average_spend:Q',
        color='group:N',
        tooltip=['group', 'average_spend']
    ).properties(
        title='Average Spend by Group'
    )
    st.altair_chart(avg_spend_chart, use_container_width=True)

    # Bounce Rate Chart
    bounce_chart = alt.Chart(results_df).mark_bar().encode(
        x='group:N',
        y='bounce_rate:Q',
        color='group:N',
        tooltip=['group', 'bounce_rate']
    ).properties(
        title='Bounce Rate by Group'
    )
    st.altair_chart(bounce_chart, use_container_width=True)
