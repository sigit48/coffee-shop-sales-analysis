"""
Coffee Shop Sales Analysis

This script analyzes coffee shop sales data to identify:
1) Top-selling menu items by revenue
2) Daily sales trend
3) Weekly sales pattern

Outputs:
- Saved charts in the `outputs/` directory
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# CONFIGURATION
# =========================
DATA_PATH = Path("data") / "coffee_sales.csv"
OUTPUT_DIR = Path("outputs")
CSV_SEPARATOR = ";"


# =========================
# UTILITY FUNCTIONS
# =========================
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Please check the file path."
        )
    return pd.read_csv(path, sep=CSV_SEPARATOR)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = {"date", "datetime", "coffee_name", "money"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if "card" in df.columns:
        df = df.drop(columns=["card"])

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
    df["coffee_name"] = df["coffee_name"].astype(str).str.strip().str.title()
    df["money"] = pd.to_numeric(df["money"], errors="coerce")

    df = df.dropna(subset=["date", "datetime", "coffee_name", "money"])
    df["day_of_week_en"] = df["date"].dt.day_name()

    return df


def save_and_show_plot(filename: str) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    filepath = OUTPUT_DIR / filename
    plt.savefig(filepath, dpi=200, bbox_inches="tight")
    plt.show()
    print(f"✔ Chart saved: {filepath}")


# =========================
# PLOTTING FUNCTIONS
# =========================
def plot_top_menu(menu_revenue: pd.Series, top_n: int = 10) -> None:
    plt.figure(figsize=(10, 6))
    menu_revenue.head(top_n).plot(kind="bar")
    plt.title(f"Top {top_n} Best-Selling Coffee Menu (by Revenue)")
    plt.xlabel("Coffee Menu")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45, ha="right")
    save_and_show_plot("top_menu_revenue.png")


def plot_daily_trend(daily_sales: pd.Series) -> None:
    plt.figure(figsize=(12, 6))
    daily_sales.plot(kind="line")
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Revenue")
    save_and_show_plot("daily_sales_trend.png")


def plot_weekly_pattern(df: pd.DataFrame) -> None:
    hari_mapping = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat",
        "Saturday": "Sabtu",
        "Sunday": "Minggu",
    }

    df = df.copy()
    df["day_of_week"] = df["day_of_week_en"].replace(hari_mapping)

    order_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    weekly_sales = (
        df.groupby("day_of_week")["money"]
        .sum()
        .reindex(order_hari)
    )

    plt.figure(figsize=(10, 6))
    weekly_sales.plot(kind="bar")
    plt.title("Weekly Sales Pattern (Revenue by Day)")
    plt.xlabel("Day")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45, ha="right")
    save_and_show_plot("weekly_sales_pattern.png")


# =========================
# MAIN EXECUTION
# =========================
def main() -> None:
    print("Coffee Shop Sales Analysis")
    print("-" * 40)

    df = load_data(DATA_PATH)
    df = clean_data(df)

    # 1) Top-selling menu
    menu_revenue = (
        df.groupby("coffee_name")["money"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Best-Selling Menu:")
    print(menu_revenue.head(10))

    top2 = menu_revenue.head(2)
    if len(top2) == 2:
        print(
            f"\nInsight:\n- Top products are '{top2.index[0]}' and "
            f"'{top2.index[1]}'. Focus promotions on these items to maximize ROI."
        )

    plot_top_menu(menu_revenue, top_n=10)

    # 2) Daily sales trend
    daily_sales = df.groupby("date")["money"].sum().sort_index()
    plot_daily_trend(daily_sales)

    # 3) Weekly pattern
    plot_weekly_pattern(df)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
