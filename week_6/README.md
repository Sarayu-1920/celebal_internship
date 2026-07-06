# Apache Spark Assignment – Week 6

## Files Included

* Week6_Practical_Assignment.ipynb – Databricks notebook containing PySpark code, outputs, and implementation of Spark concepts.
* Week6_Theory_Assignment.html – Theory questions and answers covering Spark architecture, execution, and performance concepts.

## Topics Covered

* Spark Architecture (Driver, Cluster Manager, Executors)
* Client Mode vs Cluster Mode
* Lazy Evaluation and DAG (Lineage Graph)
* Reading CSV files with schema inference
* Working with Parquet files
* DataFrame transformations and actions
* Filtering and selecting data
* Renaming columns and casting data types
* Adding new calculated columns
* Handling null values
* Predicate Pushdown
* CSV vs Parquet performance comparison
* Best practices (`show()` vs `collect()`)

## Data Processing Flow

```text
Dataset (Databricks Volume)
        ↓
Read into Spark DataFrame
        ↓
View Schema
        ↓
Select Required Columns
        ↓
Filter Data
        ↓
Rename Columns
        ↓
Cast Data Types
        ↓
Add New Column (final_price)
        ↓
Handle Null Values
        ↓
Write Processed Data (Parquet / CSV)
```

## Final Task

* Loaded the dataset from a Databricks Volume into a Spark DataFrame.
* Performed filtering and column selection using DataFrame operations.
* Renamed columns and converted data types.
* Added a calculated `final_price` column.
* Filtered null values from the dataset.
* Saved the processed data in Parquet format.
* Demonstrated Spark transformations and actions.
* Explained Spark architecture and performance concepts such as Lazy Evaluation, DAG, Predicate Pushdown, and Parquet storage.