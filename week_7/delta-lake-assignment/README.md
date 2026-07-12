# Delta Lake Assignment – Week 7

## Files Included

* `delta_merge_assignment.ipynb` – Databricks notebook containing the complete implementation of Delta Lake MERGE operations, data cleaning, validation, and outputs.
* `customer_master.csv` – Master dataset used as the target Delta table.
* `customer_incremental.csv` – Incremental dataset containing updated and new records used for the MERGE operation.
* `data_loading.png` – Screenshot of loading the CSV dataset into a Delta table.
* `data_cleaning.png` – Screenshot showing null and duplicate validation.
* `merging.png` – Screenshot of the Delta Lake MERGE operation.
* `validation.png` – Screenshot showing row count validation and MERGE verification.
* `final_output.png` – Screenshot of the final Delta table and assignment summary.

---

## Topics Covered

* Delta Lake Fundamentals
* Loading CSV data into a Delta Table
* Unity Catalog Volumes
* Data Cleaning
  * Handling Null Values
  * Removing Duplicate Records
* Creating Incremental Data
* Simulating Record Updates
* Simulating New Record Inserts
* Delta Lake MERGE
  * `WHEN MATCHED THEN UPDATE`
  * `WHEN NOT MATCHED THEN INSERT`
* Row Count Validation
* Duplicate Record Validation
* Displaying Final Delta Dataset

---

## Data Processing Flow

```text
Sample Superstore CSV
        ↓
Read CSV into Spark DataFrame
        ↓
Rename Columns
        ↓
Save as Delta Table
        ↓
Read Delta Table
        ↓
Check Null Values
        ↓
Remove Duplicate Records
        ↓
Create Incremental Dataset
        ↓
Simulate Updated Records
        ↓
Simulate New Records
        ↓
MERGE into Delta Table
        ↓
Validate Results
        ↓
Display Final Dataset
```

---

## Final Task

* Loaded the Superstore CSV dataset into a Delta table.
* Renamed columns to make them compatible with Delta Lake.
* Performed basic data quality checks for null values and duplicate records.
* Created an incremental dataset to simulate daily incoming data.
* Modified existing records to simulate updates.
* Created new records with unique `Row_ID`s to simulate inserts.
* Applied the Delta Lake `MERGE` operation using `Row_ID` as the matching key.
* Updated matching records and inserted new records into the Delta table.
* Validated the MERGE operation using row counts and duplicate checks.
* Displayed the final Delta table containing both updated and newly inserted records.

---

## Technologies Used

* Databricks
* Apache Spark (PySpark)
* Delta Lake
* Unity Catalog
* Python