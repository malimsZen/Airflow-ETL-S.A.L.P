# About

This program creates an Extraction, Transform, and Transform(ETL)  DAG that downloads the server access log files available at the URL: [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache Airflow/Build a DAG using Airflow/web-server-access-log.txt](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt)  

Resources are to be downloaded from the highlighted url, data extracted from the file, transformed to conform to the required needs, then finally loaded to the target destination.


# Table of Contents


1.1 Download  server access log file on a daily basis.

1.2 Extract task; extracts the fields `timestamp` and `visitorid`.

1.3 Transform task; Capitalizing the `visitorid`.

1.4 Load task; Compress the extracted and transformed data.

1.5 Create pipeline block.


## Task 1.1 Download
Download the text-file containing the server access logs from the mentioned resource location(url).

## Task 1.2 Extract
Two fields; 'Timestamp' and 'visitorid' are to be extracted from the log-file.

## Task 1.3 Transform
Field 'visitorid' should be transformed to upper-case. 

## Task 1.4 Load
Load task compresses both the extracted and transformed data.

## Task 1.4 Pipeline Block
The final task is to create the pipeline block of the tasks.

