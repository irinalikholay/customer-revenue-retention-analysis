-- total number of customers --

SELECT
    COUNT(DISTINCT Customer_ID) AS total_customers
FROM transactions;

-- total number of orders --

SELECT
    COUNT(DISTINCT Invoice) AS total_orders
FROM transactions;

-- average order value --

SELECT
    AVG(order_revenue) AS avg_order_value
FROM (
    SELECT
        Invoice,
        SUM(Quantity * Price) AS order_revenue
    FROM transactions
    GROUP BY Invoice
);

-- average number of order per customer --

SELECT
    AVG(num_orders) AS avg_order_per_customer
FROM (
    SELECT
        Customer_ID,
        COUNT(DISTINCT Invoice) AS num_orders
    FROM transactions
    GROUP BY Customer_ID
);

-- repeat customer rate --

SELECT
    ROUND(
        100.0 * SUM(CASE WHEN num_orders > 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS repeat_customer_rate_percent
FROM (
    SELECT
        Customer_ID,
        COUNT(DISTINCT Invoice) AS num_orders
    FROM transactions
    GROUP BY Customer_ID
);