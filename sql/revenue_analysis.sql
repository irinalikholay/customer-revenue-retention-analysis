-- revenue per order --

SELECT
    Invoice,
    SUM(Quantity *Price ) AS order_revenue
FROM transactions
GROUP BY Invoice;

-- revenue per customer --

SELECT
    Customer_ID,
    SUM(Quantity * Price) AS customer_revenue
FROM transactions
GROUP BY Customer_ID;