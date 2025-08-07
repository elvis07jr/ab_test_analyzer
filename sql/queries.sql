-- CTE to calculate the metrics for each group
WITH group_metrics AS (
    SELECT
        "group",
        COUNT(user_id) AS total_users,
        SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS converted_users,
        SUM(revenue) AS total_revenue,
        SUM(CASE WHEN bounced THEN 1 ELSE 0 END) AS bounced_users
    FROM
        users
    GROUP BY
        "group"
)

-- Final query to calculate the metrics
SELECT
    "group",
    total_users,
    converted_users,
    total_revenue,
    bounced_users,
    -- Conversion Rate: (Converted Users / Total Users) * 100
    (converted_users * 1.0 / total_users) * 100 AS conversion_rate,
    -- Average Spend: Total Revenue / Converted Users
    total_revenue / converted_users AS average_spend,
    -- Bounce Rate: (Bounced Users / Total Users) * 100
    (bounced_users * 1.0 / total_users) * 100 AS bounce_rate
FROM
    group_metrics;
