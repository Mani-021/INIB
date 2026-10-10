# INIB — Sales Data Analysis

This project analyzes the supplied `Sales Data.csv` file using Python, Pandas, and Matplotlib.

## Project contents
- `data/sales_data.csv` — input dataset supplied for analysis
- `sales_analysis.py` — cleaning, aggregation, charting, and summary script
- `outputs/` — cleaned CSV, summary tables, result summary, and charts
- `PROJECT_REPORT.md` — report with methodology and findings
- `VIDEO_DEMO_SCRIPT.md` — suggested demo walkthrough
- `LINKEDIN_POST_DRAFT.md` — draft post for the internship task

## Run locally
1. Install Python 3.9+.
2. Open a terminal in this project folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python sales_analysis.py`

## Main findings from the supplied file
- Total calculated revenue: $34,465,537.94
- Top revenue product: Macbook Pro Laptop
- Top revenue city: San Francisco
- Top revenue month: December
- Top revenue hour: 7 PM

Revenue is calculated as quantity ordered × price each; it is not profit. Check `PROJECT_REPORT.md` for the cleaning details and full results.
