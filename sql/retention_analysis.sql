DROP TABLE IF EXISTS retention_table;

CREATE TABLE retention_table AS

SELECT
    cohort_month,
    months_since_first_purchase,
    COUNT(DISTINCT Customer_ID) AS active_customers
FROM customer_cohorts
GROUP BY 
    cohort_month,
    months_since_first_purchase
ORDER BY
    cohort_month,
    months_since_first_purchase;