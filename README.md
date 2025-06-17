# aws-glue-data-pipeline

**Project Description
This project demonstrates a simple serverless ETL workflow using AWS S3, AWS Glue (PySpark), and GitHub Actions for automation.

## Workflow Overview

1. Upload data to S3
2. GitHub Action triggers AWS Glue job
3. Glue job reads, transforms, and writes output back to S3

## Technologies

- AWS S3
- AWS Glue
- GitHub Actions
- PySpark (Glue)

## Prerequisites

- AWS Account
- S3 Bucket
- AWS Glue Job
- GitHub repository with secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `GLUE_JOB_NAME`

## Project Structure

aws-glue-data-pipeline/
│
├── src/
│   └── glue_job.py               # AWS Glue ETL script
│
├──workflows/
│  └── deploy_glue.yml       # GitHub Actions workflow
│
├── data/
│   └── sample_data.csv           # Sample input data 
│
└──README.md                     # Project overview and instructions

## Setup 

```bash
# Trigger GitHub Action by pushing changes
git add .
git commit -m "trigger glue job"
git push origin main

