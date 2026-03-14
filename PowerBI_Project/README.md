# 🍫 Chocolate Shipments Sales Analytics Dashboard (Power BI)

## 📌 Project Overview
This project builds an **interactive Power BI dashboard** to analyze chocolate shipment sales data.  
The goal is to transform raw Excel data into meaningful **business insights** that help track sales performance, product demand, shipment trends, and regional distribution.

The dashboard allows users to explore **Year-on-Year sales growth, top-performing products, and shipment trends** through interactive visuals.

---

## 🎯 Business Problem
Organizations dealing with product shipments often face challenges such as:

- Difficulty tracking **overall sales performance**
- Identifying **top-performing products**
- Understanding **seasonal sales trends**
- Comparing **Year-on-Year growth**
- Monitoring **regional shipment performance**

This Power BI report solves these challenges by providing a **data-driven analytics dashboard**.

---

## 📂 Dataset
The dataset contains chocolate shipment transaction records including:

| Column | Description |
|------|------|
| Order Date | Date of shipment |
| Product | Chocolate product name |
| Category | Product category |
| Country | Shipment destination |
| Sales Person | Responsible sales representative |
| Boxes | Number of boxes shipped |
| Amount | Revenue generated |

Dataset Link:  
https://github.com/chandoo-org/Power-BI/blob/main/Telugu%20Full%20Course/sample-chocolate-shipments-data-all-Apr-2025.xlsx

---

## ⚙️ Data Processing (Power Query)
Data cleaning and transformation were performed using **Power Query**.

Key steps:

- Removed duplicates and null values
- Standardized column names
- Changed data types
- Created calculated columns
- Loaded transformed data into Power BI model

This ensures **clean and reliable data for analysis**.

---

## 🧩 Data Modeling
A **Star Schema model** was implemented for efficient analysis.

### Fact Table
- Shipments

### Dimension Tables
- Products
- Sales Person
- Calendar Table
- Geography

Relationships were created between tables using **primary and foreign keys** to optimize performance and enable advanced analytics.

---

## 📅 Calendar Table
A **Calendar table** was created to support time intelligence calculations.

Columns included:

- Year
- Month
- Quarter
- Week
- Year-Month

This enables **time-based analysis and Year-on-Year comparisons**.

---

## 📐 DAX Measures
Several **DAX measures** were created for business metrics.

### Total Sales
```DAX
Total Sales = SUM(Shipments[Amount])
