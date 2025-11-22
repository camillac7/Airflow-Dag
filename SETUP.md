# Local Airflow Setup Guide - Two Options

## ⚠️ Python Version Note

You're currently using **Python 3.13**, which is very new. Airflow has better support for **Python 3.11** or **3.12**. I've provided two options:

---

## Option A: Quick Setup with Python 3.13 (Simpler)

Try this first - Airflow 3.1.3 might work with Python 3.13.

### Run the Setup Script

```bash
./setup_airflow.sh
```

This will:
1. Install Apache Airflow 3.1.3
2. Set up your Airflow home directory
3. Initialize the database
4. Create an admin user (username: `admin`, password: `admin`)
5. Copy your DAG file to the correct location

### Start Airflow

You'll need **TWO terminals**:

**Terminal 1 - Start the Scheduler:**
```bash
export AIRFLOW_HOME=~/airflow
airflow scheduler
```

**Terminal 2 - Start the API Server:**
```bash
export AIRFLOW_HOME=~/airflow
airflow api-server --port 8080
```

**Or use standalone mode (easier - one command):**
```bash
export AIRFLOW_HOME=~/airflow
airflow standalone
```

### Access the Web UI

- Open: http://localhost:8080
- Login: `admin` / `admin`
- You should see your "basic_dag"!

---

## Option B: Using Python 3.11/3.12 (Recommended - More Stable)

If Option A doesn't work, use a virtual environment with Python 3.11 or 3.12.

### Install Python 3.11 using Homebrew

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11
brew install python@3.11
```

### Create Virtual Environment

```bash
# Navigate to your DAGS folder
cd /Users/camillacalle/Downloads/DAGS

# Create virtual environment with Python 3.11
python3.11 -m venv airflow_env

# Activate virtual environment
source airflow_env/bin/activate
```

### Install Airflow

```bash
# Upgrade pip
pip install --upgrade pip

# Install Airflow
pip install 'apache-airflow==2.9.0' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.11.txt"
```

### Initialize Airflow

```bash
# Set AIRFLOW_HOME
export AIRFLOW_HOME=~/airflow

# Initialize database
airflow db init

# Create admin user
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Copy your DAG
mkdir -p ~/airflow/dags
cp basic_dag.py ~/airflow/dags/
```

### Start Airflow (Remember to activate venv first!)

```bash
# Always activate virtual environment first
source airflow_env/bin/activate
export AIRFLOW_HOME=~/airflow

# Terminal 1
airflow scheduler

# Terminal 2 (new terminal)
source airflow_env/bin/activate
export AIRFLOW_HOME=~/airflow
airflow webserver --port 8080
```

---

## Manual Setup Steps (If Script Doesn't Work)

### 1. Install Apache Airflow

```bash
pip3 install 'apache-airflow==3.1.3'
```

### 2. Set Airflow Home Directory

```bash
export AIRFLOW_HOME=~/airflow
echo 'export AIRFLOW_HOME=~/airflow' >> ~/.zshrc
source ~/.zshrc
```

### 3. Initialize the Airflow Database

```bash
airflow db init
```

### 4. Create Admin User

```bash
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin
```

### 5. Copy Your DAG File

```bash
mkdir -p ~/airflow/dags
cp basic_dag.py ~/airflow/dags/
```

### 6. Start Airflow

**Terminal 1:**
```bash
export AIRFLOW_HOME=~/airflow
airflow scheduler
```

**Terminal 2:**
```bash
export AIRFLOW_HOME=~/airflow
airflow api-server --port 8080
```

**Or use standalone (one command for everything):**
```bash
export AIRFLOW_HOME=~/airflow
airflow standalone
```

### 7. Access the Web UI

- URL: http://localhost:8080
- Username: `admin`
- Password: `admin`

---

## Troubleshooting

### DAG Not Appearing?
- Check scheduler logs for errors
- Verify file is in `~/airflow/dags/`
- Check file has `.py` extension
- Ensure no Python syntax errors in the DAG file

### Airflow Command Not Found?
- Make sure installation completed successfully
- Try: `python3 -m airflow` instead of `airflow`
- If using virtual environment, make sure it's activated

### Python Version Issues?
- Use Option B with Python 3.11 virtual environment
- Or wait for Airflow to add Python 3.13 support

### Port 8080 Already in Use?
```bash
# Use a different port
airflow webserver --port 8081
```

---

## Quick Reference

**Stop Airflow:**
- Press `Ctrl+C` in both terminal windows

**Check DAGs folder:**
```bash
ls ~/airflow/dags/
```

**View Airflow logs:**
```bash
ls ~/airflow/logs/
```

**Check if Airflow is running:**
- Web UI: http://localhost:8080
- Or check if scheduler process is running
