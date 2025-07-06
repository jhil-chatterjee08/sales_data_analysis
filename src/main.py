from utils import load_and_merge_data, clean_data, plot_sales_trend, plot_sales_by_store
import os

print("Loading data...")
df = load_and_merge_data()

print("Cleaning data...")
df = clean_data(df)

os.makedirs("outputs", exist_ok=True)

df.to_csv("outputs/cleaned_walmart_data.csv", index=False)
print("Cleaned data saved.")

print("Creating visualizations...")
plot_sales_trend(df)
plot_sales_by_store(df)

print("Done! Plots saved in 'outputs/plots/'.")

from utils import (
    load_and_merge_data, clean_data,
    plot_sales_trend, plot_sales_by_store,
    plot_sales_by_department, plot_holiday_vs_nonholiday_sales, plot_correlation_heatmap
)
plot_sales_by_department(df)
plot_holiday_vs_nonholiday_sales(df)
plot_correlation_heatmap(df)
