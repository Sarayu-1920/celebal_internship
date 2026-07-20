# Week 8 – E-Commerce Analytics System

## Project Overview

This project simulates an end-to-end e-commerce analytics workflow using **Python, SQLite, and SQL**.

The project covers:

- Data generation
- Data cleaning
- Loading data into SQLite
- Writing analytical SQL queries
- Building a command-line reporting tool
- Handling common data quality edge cases

---

# Project Structure

```
week_8/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── database/
│   └── ecommerce.db
│
├── docs/
│
├── output/
│
├── scripts/
│
└── sql/
```

---

# Folder Explanation

## data/

Contains all CSV datasets used throughout the project.

### raw/

Original generated datasets before cleaning.

Files:

- customers.csv
- orders.csv
- order_items.csv
- products.csv

These datasets intentionally contain data quality issues that are cleaned in the next step.

---

### cleaned/

Cleaned datasets after preprocessing.

Cleaning performed includes:

- Missing value handling
- Duplicate removal
- Data type corrections
- Data validation

These files are loaded into SQLite.

---

## database/

Contains the SQLite database.

### ecommerce.db

Stores all project tables.

Tables:

- customers
- orders
- order_items
- products

All SQL queries are executed on this database.

---

## docs/

Project documentation.

### architecture.md

Explains the overall project architecture and workflow.

### implementation_notes.md

Documents implementation details, design decisions, and assumptions.

### interview_notes.md

Contains interview-focused explanations and important concepts used in this assignment.

---

## output/

### cleaning_report.txt

Summary generated during the data cleaning process.

Includes:

- Number of records processed
- Missing values handled
- Duplicates removed
- Validation summary

---

## scripts/

Contains all Python programs used in the project.

### generate_data.py

Generates synthetic e-commerce datasets.

Creates:

- customers.csv
- orders.csv
- order_items.csv
- products.csv

---

### clean_data.py

Reads raw datasets and performs data cleaning before creating cleaned datasets.

---

### load_data.py

Creates the SQLite database and loads cleaned CSV files into database tables.

---

### report_cli.py

Command-line reporting tool.

Features:

- Accepts report type
- Accepts date range
- Connects to SQLite
- Generates sales summary
- Displays top 3 products
- Compares current period with previous period

---

### test_edge_cases.py

Validates common data quality edge cases.

Checks:

- Invalid order_id values
- Discount greater than 100%
- Zero quantity
- Future order dates

---

## sql/

Contains all SQL scripts.

### schema.sql

Creates all database tables.

---

### queries.sql

Contains analytical SQL queries including:

- Revenue analysis
- Customer analytics
- Product performance
- Ranking functions
- Window functions
- Running totals
- Customer segmentation

---

### test.sql

Used to execute and validate SQL queries during development.

---

# How to Run

## 1. Generate datasets

```bash
python scripts/generate_data.py
```

---

## 2. Clean datasets

```bash
python scripts/clean_data.py
```

---

## 3. Load SQLite database

```bash
python scripts/load_data.py
```

---

## 4. Execute SQL queries

Open:

```
sql/queries.sql
```

Run the queries using SQLite.
![alt text](<screenshots/sql sc.png>)
---

## 5. Generate CLI Report

```bash
python scripts/report_cli.py
```
![alt text](<screenshots/cli sc.png>)
Provide:

- Report type
- Start date
- End date

The program displays:

- Total Orders
- Total Revenue
- Unique Customers
- Top 3 Products
- Previous Period Comparison
![alt text](<cli sc.png>)

---

## 6. Execute Edge Case Tests

```bash
python scripts/test_edge_cases.py
```

---

# Technologies Used

- Python
- SQLite
- SQL
- CSV
- Git
- GitHub

---

# Assignment Objectives Covered

- Synthetic Data Generation
- Data Cleaning Pipeline
- SQLite Database Design
- SQL Analytics
- Window Functions
- Aggregations
- Python + SQL Integration
- Command Line Reporting
- Data Validation
- Edge Case Testing

---

# Learning Outcomes

This project demonstrates practical experience with:

- Relational database design
- SQL querying
- Data preprocessing
- Python database connectivity
- Business reporting
- Data quality validation
- Version control using Git