# 🛒 Walmart Sales Data Analysis

Welcome to the Walmart Sales Data Analysis project! This project focuses on analyzing historical sales data to uncover trends, assess store and departmental performance, and examine the impact of holidays and economic indicators.

---

## 📁 Project Structure

```
sales_data_analysis/
├── data/                # Raw CSV datasets (train.csv, features.csv, stores.csv)
├── outputs/             # Cleaned data and generated plots
│   └── plots/           # PNG images of visualizations
├── src/                 # Source code
│   ├── utils.py         # Functions for loading, cleaning, and plotting
│   └── main.py          # Main script to run the workflow
├── report.docx          # Word document version of the report (optional)
└── README.md            # Overview of the project (this file)
```

---

## 🎯 Objectives

* Analyze weekly sales across different time periods
* Compare sales performance by store and department
* Examine how holidays influence sales
* Explore relationships between sales and external economic factors (CPI, unemployment, fuel prices)

---

## 🗃️ Dataset Description

The project uses the following datasets:

* **train.csv** – Weekly sales data by store and department
* **features.csv** – Contains Temperature, Fuel Price, CPI, and Unemployment
* **stores.csv** – Store-level metadata (Type, Size)

---

## 🧹 Data Processing Steps

* Merged the datasets on Store, Date, and IsHoliday
* Converted date columns into datetime format
* Forward-filled missing values
* Prepared data for plotting and correlation analysis

---

## 📊 Visualizations

The following plots were generated:

* 📈 Total Weekly Sales Over Time
* 🏪 Sales by Store
* 🧩 Sales by Department
* 🎉 Holiday vs Non-Holiday Sales
* 📊 Correlation Heatmap (Weekly Sales vs Economic Indicators)

All plots are saved in the `outputs/plots/` folder.

---

## 🔍 Key Findings

* Sales peak around major holidays (Thanksgiving, Christmas)
* Store #20 had the highest total sales
* Grocery and consumer departments dominate in volume
* Weak but visible correlation with unemployment and CPI

---

## ▶️ How to Run the Project

Make sure Python 3.x is installed. Then:

```bash
cd sales_data_analysis
python src/main.py
```

This will:

* Load and merge the datasets
* Clean the data
* Generate all visualizations and save them in `outputs/plots/`

---

## 🧠 Future Work

* Build forecasting models (e.g., ARIMA, Prophet)
* Create interactive dashboards using Power BI or Tableau
* Segment customers or stores for personalized insights

---


## 🛠 Tech Stack

* Python 3.12
* Pandas
* Matplotlib
* Seaborn
* VS Code
* Git & GitHub

---

## 👩‍💻 Author

**Jhil Chatterjee**
B.Tech IT Student | Aspiring Data Analyst

Feel free to explore, fork, or contribute to the project!
