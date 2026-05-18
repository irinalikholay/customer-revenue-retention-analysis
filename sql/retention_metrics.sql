DROP TABLE IF EXISTS retention_metrics;

CREATE TABLE retention_metrics AS

WITH cohort_size AS (
    SELECT
        cohort_month,
        active_customers AS total_customers
    FROM retention_table
    WHERE months_since_first_purchase = 0
)

SELECT
    rt.cohort_month,
    rt.months_since_first_purchase,
    rt.active_customers,
    cs.total_customers,

    ROUND(
        rt.active_customers * 100.0 / cs.total_customers,
        2
    ) AS retention_rate

FROM retention_table rt
JOIN cohort_size cs
    ON rt.cohort_month = cs.cohort_month

ORDER BY 
    rt.cohort_month,
    rt.months_since_first_purchase;