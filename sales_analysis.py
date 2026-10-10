"""
INIB - Task 1: Sales Data Analysis
Run: python sales_analysis.py
Uses the supplied Sales Data.csv file. Run from this project folder with: python sales_analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
CHARTS = OUT / "charts"
OUT.mkdir(exist_ok=True)
CHARTS.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    initial_rows = len(df)
    df.columns = [c.strip() for c in df.columns]
    # Drop an exported row-index column if present in the source CSV.
    df = df.loc[:, ~df.columns.str.match(r"^Unnamed(:\s*\d+)?$")]
    required = ["Order ID", "Product", "Quantity Ordered", "Price Each", "Order Date", "Purchase Address"]
    missing_cols = [c for c in required if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Dataset is missing expected columns: {missing_cols}")

    # Data cleaning
    df = df.dropna(subset=["Order ID", "Product", "Quantity Ordered", "Price Each", "Order Date"])
    df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors="coerce")
    df["Price Each"] = pd.to_numeric(df["Price Each"], errors="coerce")
    df = df.dropna(subset=["Quantity Ordered", "Price Each"])
    df = df[(df["Quantity Ordered"] > 0) & (df["Price Each"] >= 0)]
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df = df.dropna(subset=["Order Date"])
    df = df.drop_duplicates()
    df["Sales"] = df["Quantity Ordered"] * df["Price Each"]
    df["Month"] = df["Order Date"].dt.month
    df["Hour"] = df["Order Date"].dt.hour
    df["City"] = df["Purchase Address"].astype(str).str.split(",").str[-2].str.strip()

    # Save cleaned data and summary tables
    df.to_csv(OUT / "cleaned_sales_data.csv", index=False)
    monthly = df.groupby("Month", as_index=False)["Sales"].sum().sort_values("Month")
    monthly.to_csv(OUT / "monthly_sales.csv", index=False)
    product_sales = df.groupby("Product", as_index=False).agg(
        Units_Sold=("Quantity Ordered", "sum"), Revenue=("Sales", "sum")
    ).sort_values("Revenue", ascending=False)
    product_sales.to_csv(OUT / "product_performance.csv", index=False)
    city_sales = df.groupby("City", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
    city_sales.to_csv(OUT / "city_performance.csv", index=False)
    hourly = df.groupby("Hour", as_index=False)["Sales"].sum()
    hourly.to_csv(OUT / "hourly_sales.csv", index=False)

    # Charts
    plt.figure(figsize=(9, 5))
    plt.plot(monthly["Month"], monthly["Sales"], marker="o")
    plt.title("Monthly Sales Revenue"); plt.xlabel("Month"); plt.ylabel("Revenue")
    plt.xticks(range(1, 13)); plt.grid(True, alpha=.25); plt.tight_layout()
    plt.savefig(CHARTS / "monthly_sales.png", dpi=160); plt.close()

    top = product_sales.head(10).sort_values("Revenue")
    plt.figure(figsize=(10, 6))
    plt.barh(top["Product"], top["Revenue"])
    plt.title("Top 10 Products by Revenue"); plt.xlabel("Revenue"); plt.tight_layout()
    plt.savefig(CHARTS / "top_products.png", dpi=160); plt.close()

    top_city = city_sales.sort_values("Sales")
    plt.figure(figsize=(9, 5))
    plt.barh(top_city["City"], top_city["Sales"])
    plt.title("Sales Revenue by City"); plt.xlabel("Revenue"); plt.tight_layout()
    plt.savefig(CHARTS / "sales_by_city.png", dpi=160); plt.close()

    plt.figure(figsize=(9, 5))
    plt.bar(hourly["Hour"], hourly["Sales"])
    plt.title("Revenue by Hour of Day"); plt.xlabel("Hour (24-hour clock)"); plt.ylabel("Revenue")
    plt.xticks(range(0, 24, 2)); plt.tight_layout()
    plt.savefig(CHARTS / "sales_by_hour.png", dpi=160); plt.close()

    total_revenue = df["Sales"].sum()
    total_orders = df["Order ID"].nunique()
    total_units = df["Quantity Ordered"].sum()
    avg_order_value = total_revenue / total_orders if total_orders else 0
    best_product = product_sales.iloc[0]["Product"] if not product_sales.empty else "N/A"
    best_city = city_sales.iloc[0]["City"] if not city_sales.empty else "N/A"
    best_month = int(monthly.loc[monthly["Sales"].idxmax(), "Month"]) if not monthly.empty else 0
    summary = f"""SALES DATA ANALYSIS — RESULTS
Rows in original file: {initial_rows}
Rows after cleaning: {len(df)}
Rows removed during cleaning: {initial_rows - len(df)}
Total revenue: ${total_revenue:,.2f}
Unique orders: {total_orders}
Units sold: {total_units:,.0f}
Average revenue per order: ${avg_order_value:,.2f}
Highest-revenue product: {best_product}
Highest-revenue city: {best_city}
Highest-revenue month number: {best_month}

Source: the Sales Data.csv file supplied for this project. Figures are calculated from the cleaned records; revenue is Quantity Ordered × Price Each.
"""
    (OUT / "summary.txt").write_text(summary, encoding="utf-8")
    print(summary)
    print(f"Charts and tables saved in: {OUT}")

if __name__ == "__main__":
    main()
