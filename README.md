# Basic Airflow DAG

This directory contains a simple Apache Airflow DAG example.

## How to Use This DAG

### Option 1: Local Airflow Installation

1. **Install Airflow** (if not already installed):
   ```bash
   pip install apache-airflow
   ```

2. **Initialize Airflow** (first time only):
   ```bash
   airflow db init
   ```

3. **Find or set your DAGs folder**:
   - Default location: `~/airflow/dags/`
   - Or set `AIRFLOW_HOME` environment variable

4. **Copy the DAG file**:
   ```bash
   cp basic_dag.py ~/airflow/dags/
   # Or to your custom DAGs folder
   ```

5. **Start Airflow**:
   ```bash
   # Terminal 1: Start the scheduler
   airflow scheduler
   
   # Terminal 2: Start the webserver
   airflow webserver --port 8080
   ```

6. **Access the Web UI**:
   - Open browser: http://localhost:8080
   - Default login: `airflow` / `airflow`
   - You should see "basic_dag" in the list

### Option 2: Using Docker Compose

1. **Copy `basic_dag.py` to your Airflow Docker setup**:
   - If using official Airflow Docker image, copy to `/opt/airflow/dags/`
   - Or mount this directory as a volume in docker-compose.yml:
     ```yaml
     volumes:
       - ./DAGS:/opt/airflow/dags
     ```

2. **Restart your Airflow containers**:
   ```bash
   docker-compose restart
   ```

3. **Access the Web UI** (usually http://localhost:8080)

### Option 3: Cloud Airflow (Astro, MWAA, Composer)

- **Astro**: Upload via Astro CLI or the UI's DAG deploy feature
- **AWS MWAA**: Upload to S3 bucket configured for DAGs
- **Google Cloud Composer**: Upload to GCS bucket configured for DAGs
- **Azure**: Upload to the configured storage location

## What This DAG Does

- **Task 1 (`print_date`)**: Prints the current date using Bash
- **Task 2 (`print_hello`)**: Runs a Python function that prints "Hello from Airflow!"
- **Task 3 (`print_goodbye`)**: Prints a goodbye message using Bash

Task 1 runs first, then tasks 2 and 3 run in parallel.

## Important Notes

- **Airflow doesn't have a file upload feature in the web UI** - DAGs must be placed in the DAGs folder on the filesystem
- Airflow automatically scans the DAGs folder every few seconds
- If the DAG doesn't appear, check:
  - File is in the correct DAGs folder
  - No Python syntax errors (Airflow validates DAGs)
  - Check Airflow logs for errors
  - Ensure file is named with `.py` extension

## Troubleshooting

- **DAG not appearing**: Check Airflow scheduler logs for import errors
- **Import errors**: Ensure all required Python packages are installed
- **Permission issues**: Ensure Airflow user has read access to the DAG file

