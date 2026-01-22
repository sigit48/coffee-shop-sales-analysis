# ☕ Revenue Optimization Analysis for a Coffee Shop  
**Data-Driven Sales Insights Using Transaction-Level Data**

## 📌 Project Overview
This project analyzes coffee shop sales transaction data to identify **key revenue drivers, peak sales periods, and actionable strategies** that can support **promotion planning and revenue optimization**.

The analysis is designed from a **business decision-making perspective**, not merely exploratory analysis, simulating how a data analyst supports owners or managers in optimizing sales performance.

---

## 🧩 Business Problem
The coffee shop faces several common operational challenges:
- Promotions are run without clear data-driven prioritization
- Management lacks visibility into **which menu items truly drive revenue**
- Sales fluctuate across days, but **peak opportunities are not systematically leveraged**

**Objective:**  
Use historical transaction data to identify revenue drivers and translate insights into **clear business actions**.

---

## ❓ Key Business Questions
1. **Which coffee menu items contribute the most to total revenue?**
2. **On which days do sales peak, and how significant is the difference?**
3. **What sales patterns can be leveraged for more effective promotion strategies?**

---

## 📊 Dataset
- **Source:** Coffee shop sales transaction records
- **Format:** CSV (`;` separated)
- **Location:** `/data/coffee_sales.csv`
- **Granularity:** Transaction-level data

> The dataset is included in this repository for reproducibility.

---

## 🛠 Tools & Skills
- **Python**
- **Pandas** – data cleaning and aggregation
- **Matplotlib** – data visualization
- **Exploratory Data Analysis (EDA)**
- **Business insight translation & recommendation**

---

## 🔍 Analytical Approach

### 1. Data Preparation
- Validated column structure and data types
- Removed irrelevant fields (e.g., payment card identifiers)
- Parsed date and datetime fields
- Standardized menu item naming
- Handled missing and inconsistent values

### 2. Revenue Analysis
- Aggregated total revenue by menu item
- Identified **top-performing products** based on contribution share

### 3. Temporal Analysis
- Analyzed **daily sales trends**
- Compared revenue performance by **day of the week**
- Identified peak vs non-peak sales periods

---

## 📈 Key Insights
- A small subset of menu items accounts for a **disproportionate share of total revenue**, indicating strong product concentration
- Sales peak consistently on specific days, generating **significantly higher revenue compared to the weekly average**
- Certain low-performing menu items contribute marginal revenue while increasing operational complexity

---

## 💡 Business Recommendations
Based on the analysis:
- **Prioritize promotional campaigns** for top-revenue menu items rather than distributing discounts evenly
- **Schedule marketing activities** on peak sales days to maximize promotional ROI
- Apply **bundling strategies** combining high-performing and low-performing items to increase average transaction value
- Re-evaluate underperforming menu items for cost control or menu optimization

These actions aim to **increase revenue efficiency without increasing operational cost**.

---

## 📂 Project Structure
```text
coffee-shop-sales-analysis/
│
├── data/
│   └── coffee_sales.csv
│
├── analysis.py
├── requirements.txt
└── README.md

▶️ How to Run the Analysis
1. Install dependencies
pip install -r requirements.txt

2. Run the analysis script
python analysis.py


The script will generate:

Bar chart: Top-selling menu items by revenue
Line chart: Daily sales trend
Bar chart: Weekly sales revenue distribution


👤 Author

Sigit Dwiantoro
Data Analyst (Business-Oriented)

LinkedIn: https://www.linkedin.com/in/sigit-dwiantoro-392872227

GitHub: https://github.com/sigit48
