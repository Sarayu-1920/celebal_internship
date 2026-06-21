# Azure Data Factory Assignment – Week 4

## Files Included

* task_1.1_res_grp.png – Resource Group creation.
* task_2.1_storage_acc.png – Storage Account creation.
* task_2.2_container_with_csv.png – Blob Container with uploaded CSV file.
* task_3.1_adf.png – Azure Data Factory creation.
* task_3.2_linked_service.png – Linked Service connecting ADF and Storage Account.
* task_3.3_dataset.png – Source and Destination datasets.
* task_3.4_get_metadata.png – Get Metadata activity configuration.
* task_4.1_pipeline_design.png – Pipeline design using Get Metadata and Copy Data activities.
* task_5.1_pipeline_succeeded.png – Successful pipeline execution.
* task_5.2_pipeline_blob_output.png – Output file generated in Blob Storage.
* task_6.1_iam_roles.png – IAM role assignments for ADF Managed Identity.

## Tasks Done

* Created an Azure Resource Group to organize project resources.
* Created an Azure Storage Account with Data Lake Storage Gen2 enabled.
* Created a Blob Container and uploaded the `Sample-Superstore.csv` file.
* Created an Azure Data Factory (ADF) instance.
* Explored ADF Studio sections: Author, Monitor, and Manage.
* Created a Linked Service to connect ADF with Azure Blob Storage.
* Created Source and Destination datasets for the pipeline.
* Configured a Get Metadata activity to validate source file information.
* Built a pipeline using Get Metadata and Copy Data activities.
* Configured source and destination datasets in the Copy Data activity.
* Validated and published the pipeline.
* Executed the pipeline using Debug mode.
* Successfully copied data from `Sample-Superstore.csv` to `output.csv`.
* Verified pipeline execution status in ADF Monitor.
* Assigned IAM roles to the Azure Data Factory Managed Identity.
* Granted Storage Blob Data Contributor access to Azure Storage.

## Pipeline Flow

```text
Sample-Superstore.csv
        ↓
Azure Blob Storage
        ↓
Linked Service
        ↓
Source Dataset
        ↓
Get Metadata
        ↓
Copy Data
        ↓
Destination Dataset
        ↓
output.csv
```

## Final Task (Mini Project)

* Built an end-to-end data pipeline using Azure Blob Storage and Azure Data Factory.
* Used `Sample-Superstore.csv` stored in Blob Storage as the source file.
* Created a Linked Service to establish connectivity between ADF and Azure Storage.
* Created Source and Destination datasets for file processing.
* Used Get Metadata activity to validate source file information before execution.
* Used Copy Data activity to move data from the source file to a new destination file (`output.csv`).
* Successfully executed the pipeline and verified the output file in Blob Storage.
* Implemented secure access using Azure Data Factory Managed Identity and IAM role assignments.

## Brief Insights

* Azure Resource Groups help organize and manage related cloud resources.
* Azure Blob Storage is used to store and access files in the cloud.
* Linked Services and Datasets act as the connection and data representation layers in Azure Data Factory.
* Get Metadata activity can be used to validate and inspect source files before processing.
* Copy Data activity enables data movement between source and destination locations.
* Azure Data Factory pipelines help automate end-to-end data workflows.
* Managed Identity and Azure RBAC provide secure, role-based access to Azure resources.
