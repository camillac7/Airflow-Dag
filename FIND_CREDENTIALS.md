# How to Get Your Airflow Login Credentials

## Option 1: Run Standalone and See Credentials (Recommended)

Since Airflow 3.x creates credentials automatically when you start standalone mode, run this in your terminal:

```bash
export AIRFLOW_HOME=~/airflow
airflow standalone
```

**Watch the terminal output!** You'll see something like:

```
...
Admin user created!
Username: admin
Password: xyz123...
...
```

Copy those credentials and use them to login at http://localhost:8080

---

## Option 2: Create User Through Web UI

1. Start Airflow:
   ```bash
   export AIRFLOW_HOME=~/airflow
   airflow standalone
   ```

2. Open http://localhost:8080 in your browser

3. If Airflow prompts you to create the first admin user:
   - Fill in the form with:
     - Username: `admin`
     - Email: `admin@example.com`
     - Password: `admin` (or choose your own)
     - Other required fields

4. Click "Create" and you'll be logged in!

---

## Quick Start Script

I've created a script for you. Run this in your terminal:

```bash
cd /Users/camillacalle/Downloads/DAGS
./start_airflow.sh
```

This will start Airflow and show you the credentials.

