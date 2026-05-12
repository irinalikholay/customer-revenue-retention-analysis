DROP TABLE IF EXISTS customer_cohorts;

CREATE TABLE customer_cohorts AS

WITH first_purchase AS (
    SELECT
        Customer_ID,
        MIN(date(InvoiceDate)) AS first_purchase_date
    FROM transactions
    GROUP BY Customer_ID
)

SELECT 
    t.Customer_ID,

    strftime('%Y-%m', fp.first_purchase_date) AS cohort_month,
    strftime('%Y-%m', t.InvoiceDate) AS purchase_month,

    (
        (CAST(strftime('%Y', t.InvoiceDate) AS INTEGER) - 
         CAST(strftime('%Y', fp.first_purchase_date) AS INTEGER)) * 12 

        +

        (CAST(strftime('%m', t.InvoiceDate) AS INTEGER) - 
         CAST(strftime('%m', fp.first_purchase_date) AS INTEGER))
    ) AS months_since_first_purchase

FROM transactions t
JOIN first_purchase fp
    ON t.Customer_ID = fp.Customer_ID;