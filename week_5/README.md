# Apache Spark Assignment – Week 5

## Files Included

* Week5_Spark.ipynb – Databricks notebook containing all theory answers, PySpark code, outputs, and insights.
* Sales.csv – Synthetic retail sales dataset with 1000 records used for Spark operations.

## Tasks Done

* Learned the limitations of MapReduce and advantages of Apache Spark.
* Understood how Spark uses in-memory computing for faster processing.
* Loaded the retail sales dataset into Spark DataFrame.
* Removed duplicate records using `dropDuplicates()`.
* Filtered data based on conditions such as region, age, and subscription type.
* Handled missing values using `na.fill()` and `na.drop()`.
* Performed aggregations using `count()`, `sum()`, `avg()`, `min()`, and `max()`.
* Grouped data using `groupBy()` and applied conditions on aggregated results.
* Modified the schema by converting timestamp columns and renaming columns.
* Removed records with invalid or incomplete data.
* Built a complete data processing pipeline using Spark DataFrames.

## Data Processing Flow

```text
Sales.csv
    ↓
Load into Spark DataFrame
    ↓
Data Cleaning
(Remove Duplicates, Handle Null Values)
    ↓
Filtering
    ↓
Schema Modification
    ↓
Aggregation & groupBy
    ↓
Final Processed Data
```

## Final Task

* Imported the retail sales dataset into Databricks.
* Performed data cleaning by removing duplicate records and handling null values.
* Applied filters on different columns such as region, age, and subscription.
* Calculated summary statistics using aggregate functions.
* Grouped data by city and store to generate business insights.
* Converted timestamp data into Spark TimestampType.
* Created a complete Spark data processing pipeline combining cleaning and aggregation.
