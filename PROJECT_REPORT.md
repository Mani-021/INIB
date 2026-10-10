# Sales Data Analysis — Internship Project Report

## 1. Objective
Analyze sales transactions to identify monthly sales patterns, top-performing products, city-level performance, and high-revenue hours. The findings can help a business plan inventory, marketing, and staffing.

## 2. Dataset
- Input file: `data/sales_data.csv` (the Sales Data.csv file supplied for this project)
- Rows in source file: 185,950
- Fields include order ID, product, quantity, unit price, order date, purchase address, month, sales, city, and hour.
- The source also contained an exported row-index column (`Unnamed: 0`), which is excluded from the analysis.

## 3. Tools
Python, Pandas, Matplotlib. See `requirements.txt`.

## 4. Methodology
1. Load the CSV and normalize column names.
2. Drop the exported row-index column.
3. Remove records with missing or invalid required values, non-positive quantities, negative unit prices, or invalid dates.
4. Remove duplicate records.
5. Calculate revenue as `Quantity Ordered × Price Each`; derive month, hour, and city from the order date and purchase address.
6. Aggregate revenue and units by month, product, city, and hour.
7. Export cleaned data, summary tables, and visualizations to `outputs/`.

## 5. Results
The analysis retained **185,686 rows** and removed **264 rows** during cleaning.

- **Total calculated revenue:** $34,465,537.94
- **Unique order IDs:** 178,437
- **Units sold:** 208,812
- **Average revenue per unique order ID:** $193.15
- **Highest-revenue product:** Macbook Pro Laptop ($8,032,500.00)
- **Highest-revenue city:** San Francisco ($8,254,743.55)
- **Highest-revenue month:** December (month 12), with $4,608,295.70
- **Highest-revenue hour:** 7 PM (19:00), with $2,411,971.14

## 6. Interpretation and recommendations
- Macbook Pro Laptop generated the most revenue in the cleaned data. Review its inventory and promotions, while also considering unit volume and profit margin.
- December had the highest monthly revenue. This suggests checking holiday-season demand and planning stock and campaign timing accordingly.
- San Francisco was the top city by revenue. Compare regional demand and marketing costs before reallocating budget.
- 7 PM was the strongest hour by revenue among the hourly groups. Consider aligning customer support or promotional timing with observed demand.
- Revenue is not profit: costs, returns, discounts, and margin data were not included in this analysis.

## 7. Deliverables
- `sales_analysis.py` — repeatable analysis script
- `outputs/cleaned_sales_data.csv` — cleaned records
- `outputs/monthly_sales.csv`, `product_performance.csv`, `city_performance.csv`, `hourly_sales.csv` — aggregated results
- `outputs/charts/` — generated charts
- `outputs/summary.txt` — console-style result summary

## 8. How to run
From this project folder:
```bash
pip install -r requirements.txt
python sales_analysis.py
```

## 9. Conclusion
This project demonstrates data cleaning, date/time feature extraction, grouping and aggregation, summary metric calculation, and visualization using Python. Results above are calculated from the supplied Sales Data.csv file and should be described as sales revenue analysis, not profit analysis.
