import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_merge_data():
    train = pd.read_csv(r'D:\sales_data_analysis\data\train.csv')
    features = pd.read_csv(r'D:\sales_data_analysis\data\features.csv')
    stores = pd.read_csv(r'D:\sales_data_analysis\data\stores.csv')

    df = pd.merge(train, features, on=['Store', 'Date', 'IsHoliday'], how='left')
    df = pd.merge(df, stores, on='Store', how='left')

    df['Date'] = pd.to_datetime(df['Date'])

    return df

def clean_data(df):
    df.ffill(inplace=True)
    return df

def plot_sales_trend(df):
    sales_by_date = df.groupby('Date')['Weekly_Sales'].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=sales_by_date, x='Date', y='Weekly_Sales', color='darkviolet')
    plt.title("Total Weekly Sales Over Time", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.tight_layout()

    os.makedirs('outputs/plots', exist_ok=True)
    plt.savefig('outputs/plots/weekly_sales_trend.png')
    plt.close()

def plot_sales_by_store(df):
    sales_by_store = df.groupby('Store')['Weekly_Sales'].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Store', y='Weekly_Sales', data=sales_by_store, color='mediumseagreen')
    plt.title("Total Sales by Store", fontsize=14)
    plt.xlabel("Store")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    plt.savefig('outputs/plots/sales_by_store.png')
    plt.close()

def plot_sales_by_department(df):
    dept_sales = df.groupby('Dept')['Weekly_Sales'].sum().reset_index()
    dept_sales = dept_sales.sort_values(by='Weekly_Sales', ascending=False)

    plt.figure(figsize=(14, 6))
    sns.barplot(x='Dept', y='Weekly_Sales', data=dept_sales, color='salmon')
    plt.title("Total Sales by Department", fontsize=14)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('outputs/plots/sales_by_department.png')
    plt.close()

def plot_holiday_vs_nonholiday_sales(df):
    holiday_sales = df.groupby('IsHoliday')['Weekly_Sales'].sum().reset_index()
    holiday_sales['IsHoliday'] = holiday_sales['IsHoliday'].map({False: 'Non-Holiday', True: 'Holiday'})

    plt.figure(figsize=(6, 5))
    sns.barplot(
        data=holiday_sales,
        x='IsHoliday',
        y='Weekly_Sales',
        hue='IsHoliday',  
        palette={'Holiday': 'darkred', 'Non-Holiday': 'steelblue'},
        legend=False       
    )
    plt.title("Holiday vs Non-Holiday Sales", fontsize=14)
    plt.xlabel("Is Holiday")
    plt.ylabel("Total Weekly Sales")
    plt.tight_layout()
    plt.savefig('outputs/plots/holiday_vs_nonholiday.png')
    plt.close()


def plot_correlation_heatmap(df):
    corr_cols = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    df_corr = df[corr_cols].dropna()
    corr = df_corr.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='icefire', fmt=".2f", square=True, linewidths=0.5, cbar_kws={"shrink": .75})
    plt.title("Correlation Heatmap", fontsize=14)
    plt.tight_layout()
    plt.savefig('outputs/plots/correlation_heatmap.png')
    plt.close()


