# A/B Test Analyzer

This project is a Streamlit application for analyzing A/B test data. It allows users to upload a CSV file with their experiment data and view the results of the analysis, including statistical significance.

## Features

- **SQL Analysis:** Calculates key metrics like conversion rate, average spend, and bounce rate using DuckDB for in-memory SQL execution.
- **Statistical Analysis:** Performs lift analysis using t-tests to determine the statistical significance of the results.
- **Interactive Visualizations:** Uses Altair to create interactive charts for comparing the performance of the two groups.
- **User-Friendly Interface:** Provides a simple and intuitive web interface built with Streamlit.

## How to Use

1.  **Install Dependencies:**
    Make sure you have Python 3.7+ installed. Then, install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application:**
    To start the Streamlit application, run the following command in your terminal:
    ```bash
    streamlit run streamlit_app/app.py
    ```

3.  **Upload and Analyze:**
    - Open the application in your web browser.
    - Click on the "Browse files" button to upload your A/B test data in CSV format.
    - The application will automatically process the data and display the results.

## Interpreting the Results

The application provides three main sections of results:

-   **A/B Test Metrics:** A summary table of the key metrics for each group (A and B), including conversion rate, average spend, and bounce rate.
-   **Statistical Significance (p-values):** The p-value for each metric, which indicates the probability of observing the data if there were no real difference between the groups.
    -   A **p-value less than 0.05** is generally considered statistically significant, meaning there is a high probability that the observed difference is real and not due to random chance.
-   **Visualizations:** Bar charts that visually compare the performance of the two groups for each metric.

## Business Impact

The results of the A/B test analysis can help you make data-driven decisions about your product. For example:

-   If the new version (Group B) shows a statistically significant increase in conversion rate, you can confidently roll out the change to all users.
-   If there is no significant difference between the two versions, you may decide to stick with the original version or run another test with a more significant change.
-   By analyzing the average spend, you can understand the impact of the changes on user revenue.
-   The bounce rate analysis can help you identify if the changes are causing users to leave your site more frequently.
