Customer Revenue & Retention Analysis

In this project I analyze customer behavior using translation data.

My goal is to understand:
- how customers return over time (retention)
- how much revenue they generate
- which cohorts perform better

Tools:
- SQL
- Python (pandas)
- Visualization (matplotlib/seaborn)

### DATA EXPLORATION ###

My goal is to understand dataset structure and check data quality.

What was done:
- Loaded dataset
- Checked shape and columns
- Checked missing values
- Found negative values and cancelled orders

Result:
Dataset contains missing CustomerID and invalid transactions (negative quantity, cancelled invoices)

*File:
`src/explore_data.py`

### DATA CLEANING ###

Clean dataset and remove invalid transaction.

What was done:
- Removed missing Customer_ID
- Filtered negative quantity
- Removed zero/negative prices
- Excluded cancelled invoices
- Converted date column 

*File:
`src/data_cleaning.py`

### LOAD TO SQL & REVENUE CALCULATION 

Load cleaned data into database and calculated revenue

What was done:
- Loaded data into SQLite
- Created `transactions` table
- Calculated revenue per order 
- Calculated revenue per customer

As a result , prepared revenue metrics for further analysis

*Files:
`src/load_to_sql.py`
`sql/revenue_analysis.sql`

### CUSTOMER ANALYSIS ###

Goal of this step, is to understand customer behavior

What was done:
- Calculated number of customers and orders 
- Measured average order value 
- Analyzed orders per customer
- calculated repeat customer rate 

Key Metrics:
- Total customers: 5,878
- Total orders: 36,969
- Average order value: ~480
- Average orders per customer: ~6.3
- Repeat customer rate: 72.39%

# Insights
The business shows strong customer engagement and retention.
On average, each customer makes more than 6 purchases, which indicates high loyalty.

A repeat customer rate above 70% suggests that most users return after their first purchase, highlighting a strong product-market fit and effective customer retention strategy.