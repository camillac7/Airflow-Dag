# Quick Start Guide - Your Airflow is Ready! 🚀

## ✅ What's Fixed

1. ✅ Database has been reinitialized and migrated
2. ✅ DAG file is in place at `~/airflow/dags/basic_dag.py`
3. ✅ Airflow 3.1.3 is installed

## 🎯 Next Steps

### Option A: Standalone Mode (Easiest - One Command!)

Run everything in a single terminal:

```bash
export AIRFLOW_HOME=~/airflow
airflow standalone
```

This starts the scheduler, API server, and everything else in one go. It will also automatically create an admin user and show you the credentials!

---

### Option B: Separate Processes (Two Terminals)

If you prefer to run components separately:

#### 1. Start the Scheduler (Terminal 1)

```bash
export AIRFLOW_HOME=~/airflow
airflow scheduler
```

Keep this terminal open - it needs to keep running.

#### 2. Start the API Server (Terminal 2)

Open a **NEW terminal window** and run:

```bash
export AIRFLOW_HOME=~/airflow
airflow api-server --port 8080
```

Keep this terminal open too.

**Note:** In Airflow 3.x, `airflow webserver` has been replaced with `airflow api-server`.

### 3. Access the Web UI

1. Open your browser: **http://localhost:8080**
2. **Create your admin user** (Airflow 3.x will prompt you):
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `admin` (or choose your own)
   - Fill in other fields as needed

3. After creating the user, you'll be logged in
4. You should see your **"basic_dag"** in the DAGs list!

## 🎉 That's It!

Your DAG is ready to use. You can:
- Click on the DAG name to view details
- Toggle it ON to enable scheduling
- Trigger a manual run using the play button ▶️

## ⚠️ Important Notes

- **Keep both terminals running** - don't close them while using Airflow
- **Stop Airflow**: Press `Ctrl+C` in both terminals
- If you see errors, check the terminal outputs for details

## 🔍 Troubleshooting

**Database error fixed?** ✅ Yes - the database was reinitialized

**DAG not appearing?**
- Wait 30-60 seconds for the scheduler to scan DAGs
- Check scheduler terminal for any errors
- Verify the file is at: `~/airflow/dags/basic_dag.py`

**Can't access web UI?**
- Make sure the webserver is running (Terminal 2)
- Check if port 8080 is available
- Try: http://127.0.0.1:8080 instead

## 📝 Your DAG Details

- **DAG ID**: `basic_dag`
- **Schedule**: Runs daily
- **Tasks**:
  1. `print_date` - Prints current date
  2. `print_hello` - Prints "Hello from Airflow!"
  3. `print_goodbye` - Prints goodbye message

