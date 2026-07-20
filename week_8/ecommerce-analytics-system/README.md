# Week 8 – E-Commerce Analytics System

## Project Overview

This project demonstrates an end-to-end E-Commerce Analytics System built using **Python, SQLite, and SQL**. It simulates a real-world data engineering workflow from data generation to reporting.

The project includes:

- Synthetic data generation
- Data cleaning
- SQLite database creation
- Analytical SQL queries
- Python + SQL integration
- Command Line reporting tool
- Edge case validation

---

# Project Structure

```
ecommerce-analytics-system/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── database/
│   └── ecommerce.db
│
├── output/
│   └── cleaning_report.txt
│
├── screenshots/
│   ├── cli sc.png
│   └── sql sc.png
│
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_data.py
│   ├── report_cli.py
│   └── test_edge_cases.py
│
├── sql/
│   ├── schema.sql
│   ├── queries.sql
│   └── test.sql
│
├── README.md
└── ecommerce.db
```

---

# Folder Description

## data/

Contains all datasets used in the project.

### raw/

Stores the original generated CSV files.

Files:

- customers.csv
- orders.csv
- order_items.csv
- products.csv

These datasets are produced by `generate_data.py`.

---

### cleaned/

Stores cleaned datasets after preprocessing.

Cleaning includes:

- Missing value handling
- Duplicate removal
- Data validation
- Standardization

These files are loaded into SQLite.

---

## database/

Contains the SQLite database.

### ecommerce.db

Stores all project tables:

- customers
- orders
- order_items
- products

This database is used for SQL analytics and reporting.

---

## output/

### cleaning_report.txt

Generated during data cleaning.

Includes:

- Records processed
- Missing values handled
- Duplicate records removed
- Cleaning summary

---

## screenshots/

Contains screenshots demonstrating the project.

### cli sc.png

Output of the command-line reporting tool.

### sql sc.png

Execution of SQL analytical queries.

---

## scripts/

Python scripts implementing the complete pipeline.

### generate_data.py

Generates synthetic e-commerce datasets.

Output:

- Raw CSV files

---

### clean_data.py

Reads raw datasets and creates cleaned datasets.

Output:

- Cleaned CSV files
- Cleaning report

---

### load_data.py

Creates SQLite tables and loads cleaned CSV data into the database.

---

### report_cli.py

Python + SQLite integration.

Features:

- Accepts report type
- Accepts date range
- Connects to SQLite
- Calculates:
  - Total Orders
  - Total Revenue
  - Unique Customers
- Displays Top 3 Products
- Compares current period with previous period

---

### test_edge_cases.py

Performs basic data quality validation.

Checks:

- Invalid order_id values
- Discount percentage greater than 100
- Zero quantity
- Future order dates

---

## sql/

Contains all SQL scripts.

### schema.sql

Creates all required database tables.

---

### queries.sql

Contains analytical SQL queries covering:

- Aggregations
- Joins
- CTEs
- Window Functions
- Ranking Functions
- Running Totals
- Customer Segmentation
- Business Analytics

---

### test.sql

Used during development for testing and validating SQL queries.

---

# How to Run

## Step 1 – Generate Dataset

```bash
python scripts/generate_data.py
```

---

## Step 2 – Clean Dataset

```bash
python scripts/clean_data.py
```

---

## Step 3 – Load SQLite Database

```bash
python scripts/load_data.py
```

---

## Step 4 – Execute SQL Queries

Open and execute:

```
sql/queries.sql
```

against

```
database/ecommerce.db
```

---

## Step 5 – Run CLI Report

```bash
python scripts/report_cli.py
```
![alt text](<screenshots/sql sc.png>)
Provide:

- Report Type
- Start Date
- End Date

Example:

```
Report Type : monthly
Start Date  : 2024-01-01
End Date    : 2024-01-31
```

The report displays:

- Total Orders
- Revenue
- Unique Customers
- Top 3 Products
- Previous Period Comparison

---

## Step 6 – Validate Edge Cases

```bash
python scripts/test_edge_cases.py
```
![alt text](<screenshots/cli sc.png>)
This validates:

- Missing parent orders
- Invalid discounts
- Zero quantity
- Future order dates

---

# Technologies Used

- Python
- SQLite
- SQL
- CSV
- Git
- GitHub

---

# Assignment Coverage

This project satisfies all Week 8 assignment requirements:

- Synthetic Data Generation
- Data Cleaning Pipeline
- SQLite Database Design
- SQL Analytics
- Window Functions
- Python + SQL Integration
- Command Line Reporting
- Edge Case Validation
- Business Reporting

---

# Learning Outcomes

This project demonstrates practical knowledge of:

- Relational Database Design
- SQL Query Writing
- Window Functions
- Data Cleaning
- SQLite Integration with Python
- Business Report Generation
- Data Validation
- Git Version Control