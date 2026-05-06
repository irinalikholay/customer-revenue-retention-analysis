-- Create LTV table --
DROP TABLE IF EXISTS customer_ltv;

CREATE TABLE customer_ltv AS
SELECT
    Customer_ID,
    SUM(Quantity * Price) AS customer_ltv
FROM transactions
GROUP BY Customer_ID;

-- Average LTV --

SELECT
    AVG(customer_ltv) AS avg_ltv
FROM customer_ltv;

-- LTV distribution --

SELECT
    CASE
        WHEN customer_ltv < 100 THEN 'Low Value'
        WHEN customer_ltv BETWEEN 100 AND 1000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS customer_segment,
    COUNT(*) AS num_customers
FROM customer_ltv
GROUP BY customer_segment
ORDER BY num_customers DESC;