# Coffee Shop Sales Analysis (EDA)

This project analyzes coffee shop sales transactions to identify top-selling menu items, sales trends, and actionable business insights for promotion strategy and revenue optimization.

## Business Questions
1. Which coffee menu contributes the most to revenue?
2. On which days does sales peak?
3. What patterns can be used for promotion strategy?

## Dataset
- Source: Coffee shop sales transactions (CSV)
- File path: `data/coffee_sales.csv`
- Separator: `;`

> Note: The dataset is included in this repository (see `/data` folder).

## Tools & Skills
- Python
- Pandas (data cleaning & analysis)
- Matplotlib (visualization)
- EDA (exploratory data analysis)
- Business insight & recommendations

## Project Structure
```text
coffee-sales-analysis/
│
├── data/
│   └── coffee_sales.csv
│
├── analysis.py
├── requirements.txt
└── README.md
Key Steps
Load and validate dataset columns

Data cleaning:

Remove irrelevant columns (e.g., card)

Parse date and datetime

Standardize menu names

Handle missing/invalid values

Analysis:

Top-selling coffee menu by total revenue

Daily sales trend

Weekly sales pattern

Outputs
The script produces:

Bar chart: Top-selling menu items by total revenue

Line chart: Daily sales trend

Bar chart: Weekly sales pattern (revenue by day)

How to Run
1) Install dependencies
bash
Copy code
pip install -r requirements.txt
2) Run the analysis
bash
Copy code
python analysis.py
Business Recommendations (Example)
Prioritize promotions for top-performing menu items

Schedule marketing campaigns on peak sales days

Use bundling strategy to increase average transaction value

Author
Sigit Dwiantoro

LinkedIn: https://www.linkedin.com/in/sigit-dwiantoro-392872227

GitHub: https://github.com/sigit48