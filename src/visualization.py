import pandas as pd
import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "customer_revenue.db"
OUTPUT_PATH = BASE_DIR / "outputs" / "retention_heatmap.png"


def create_retention_heatmap():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        cohort_month,
        months_since_first_purchase,
        retention_rate
    FROM retention_metrics
    """


    df = pd.read_sql(query, conn)
    conn.close()


    retention_pivot = df.pivot(
        index="cohort_month",
        columns="months_since_first_purchase",
        values="retention_rate"
    )


    plt.figure(figsize=(16, 9))


    sns.heatmap(
        retention_pivot,
        cmap="Blues",
        annot=True,
        fmt=".1f",
        linewidths=0.5,
        cbar_kws={"label": "Retention Rate (%)"}
    )


    plt.title("Monthly Customer Retention Cohort Analysis")
    plt.xlabel("Months Since First Purchase")
    plt.ylabel("Cohort Month")


    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)


    print("Retention heatmap saved successfully!")


def create_ltv_distribution():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        CASE
            WHEN customer_ltv < 100 THEN 'Low Value'
            WHEN customer_ltv BETWEEN 100 AND 1000 THEN 'Medium Value'
            ELSE 'High Value'
        END AS customer_segment,
        COUNT(*) AS num_customers
    FROM customer_ltv
    GROUP BY customer_segment
    """

    df = pd.read_sql(query, conn)
    conn.close()

    segment_order = ["Low Value", "Medium Value", "High Value"]
    df["customer_segment"] = pd.Categorical(
        df["customer_segment"],
        categories=segment_order,
        ordered=True
    )
    df = df.sort_values("customer_segment")

    total_customers = df["num_customers"].sum()
    df["percentage"] = (df["num_customers"] / total_customers * 100).round(1)

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        df["customer_segment"],
        df["num_customers"],
        width=0.9,
        color=["#d9534f", "#f0ad4e", "#5cb85c"]
    )

    for bar, (_, row) in zip(bars, df.iterrows()):
        height = bar.get_height()

        if height < 500:
            y_position = height + 120
            text_color = "black"
        else:
            y_position = height / 2
            text_color = "white"

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y_position,
            f'{row["num_customers"]}\n({row["percentage"]}%)',
            ha='center',
            va='center',
            fontsize=11,
            fontweight='bold',
            color=text_color
        )

    plt.title(
        "Customer Segmentation by Lifetime Value",
        fontsize=16,
        fontweight='bold'
    )
    plt.xlabel("Customer Segment", fontsize=12)
    plt.ylabel("Number of Customers", fontsize=12)

    plt.ylim(0, 3200)

    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()

    plt.savefig(BASE_DIR / "outputs" / "ltv_distribution.png", dpi=300)

    print("LTV Distribution saved successfully!")


def create_top_customers_chart():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        Customer_ID,
        customer_ltv
    FROM customer_ltv
    ORDER BY customer_ltv DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)
    conn.close()

    df["Customer_ID"] = df["Customer_ID"].astype(int).astype(str)
    df = df.sort_values("customer_ltv", ascending=False)

    plt.figure(figsize=(12, 7))

    ax = sns.barplot(
        data=df,
        x="customer_ltv",
        y="Customer_ID",
        orient="h",
        color="#4c72b0"
    )

    plt.title("Top 10 Customers by Lifetime Value", fontsize=16, fontweight="bold")
    plt.xlabel("Customer Lifetime Value")
    plt.ylabel("Customer ID")

    for i, row in df.iterrows():
        ax.text(
            row["customer_ltv"] + 10000,
            i,
            f'{row["customer_ltv"]:,.0f}',
            va="center",
            fontsize=10
        )

    plt.grid(axis="x", alpha=0.3)
    sns.despine()
    plt.subplots_adjust(left=0.18, right=0.92)

    plt.savefig(BASE_DIR / "outputs" / "top_customers.png", dpi=300)
    plt.close()

    print("Top customers chart saved successfully!")


def create_revenue_over_time_chart():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        substr(InvoiceDate, 1, 7) AS month,
        ROUND(SUM(Quantity * Price), 2) AS revenue
    FROM transactions
    GROUP BY month
    ORDER BY month
    """


    df = pd.read_sql(query, conn)
    conn.close()

    plt.figure(figsize=(12, 7))

    ax = sns.lineplot(
        data=df,
        x="month",
        y="revenue",
        marker="o",
        linewidth=3,
        color="#4c72b0"
    )

    plt.title(
        "Revenue Over Time",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Revenue (£)", fontsize=12)

    ax.ticklabel_format(style='plain', axis='y')

    plt.xticks(rotation=45)

    plt.grid(alpha=0.3)
    sns.despine()

    plt.tight_layout()

    plt.savefig(
        BASE_DIR / "outputs" / "revenue_over_time.png",
        dpi=300
    )

    print("Revenue over time chart saved successfully!")


create_retention_heatmap()
create_ltv_distribution()
create_top_customers_chart()
create_revenue_over_time_chart()