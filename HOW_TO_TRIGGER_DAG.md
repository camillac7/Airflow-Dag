# How to Trigger Your DAG

## What Your DAG Does

Your `basic_dag` performs these tasks in order:

1. **Task 1: `print_date`**
   - Runs a bash command to print the current date
   - Example output: `Fri Nov 22 01:45:00 EST 2024`

2. **Task 2: `print_hello`** (runs after Task 1)
   - Runs a Python function that prints "Hello from Airflow!"
   - Returns: "Hello World"

3. **Task 3: `print_goodbye`** (runs in parallel with Task 2, after Task 1)
   - Runs a bash command to print "Goodbye from Airflow!"

**Task Flow:**
```
Task 1 (print_date)
    ├──> Task 2 (print_hello)
    └──> Task 3 (print_goodbye)
```

Task 1 runs first, then Tasks 2 and 3 run at the same time (in parallel).

---

## How to Trigger the DAG

### Method 1: Using the Airflow Web UI (Easiest)

1. **Open Airflow Web UI**
   - Go to: http://localhost:8080
   - Login with your credentials

2. **Find Your DAG**
   - Look for `basic_dag` in the DAGs list
   - Make sure the toggle switch is **ON** (green) on the left side

3. **Trigger the DAG**
   - Click on the DAG name `basic_dag` to open it
   - Click the **▶️ Play Button** (Trigger DAG) in the top right
   - A popup will appear - click **"Trigger"**

4. **Watch It Run**
   - You'll see the DAG run appear in the "Runs" section
   - Click on the run to see the task graph
   - Tasks will change color as they run:
     - **Gray** = Not started
     - **Light Blue** = Queued
     - **Dark Blue** = Running
     - **Green** = Success
     - **Red** = Failed

5. **View Logs**
   - Click on any task (box) in the graph
   - Click **"Log"** to see the output
   - You'll see the date, "Hello from Airflow!", and "Goodbye from Airflow!" messages

---

### Method 2: Using Airflow CLI

Open a terminal and run:

```bash
export AIRFLOW_HOME=~/airflow
airflow dags trigger basic_dag
```

This will trigger the DAG immediately.

---

### Method 3: Using the Airflow API

```bash
curl -X POST "http://localhost:8080/api/v1/dags/basic_dag/dagRuns" \
  -H "Content-Type: application/json" \
  -d '{"conf": {}}'
```

---

## Understanding the DAG Run

### What Happens When You Trigger:

1. **DAG Run Created**: Airflow creates a new DAG run instance
2. **Task 1 Starts**: `print_date` runs and prints the current date
3. **Task 1 Completes**: Once done, it triggers Tasks 2 and 3
4. **Tasks 2 & 3 Run**: Both start at the same time (parallel execution)
5. **All Tasks Complete**: DAG run finishes successfully

### Expected Output:

**Task 1 Log:**
```
Fri Nov 22 01:45:00 EST 2024
```

**Task 2 Log:**
```
Hello from Airflow!
```

**Task 3 Log:**
```
Goodbye from Airflow!
```

---

## Schedule vs Manual Trigger

- **Scheduled Runs**: Your DAG is set to run daily (every 24 hours) automatically
- **Manual Triggers**: You can trigger it anytime using the methods above

To disable automatic scheduling:
- Toggle the DAG **OFF** in the UI
- Or change `schedule=timedelta(days=1)` to `schedule=None` in the DAG file

---

## Troubleshooting

**DAG not appearing?**
- Wait 30-60 seconds for the scheduler to scan
- Check for errors in the DAG (red circle icon)
- Check scheduler logs

**Can't trigger?**
- Make sure the DAG toggle is ON
- Check that Airflow scheduler is running
- Verify no syntax errors in the DAG

**Tasks failing?**
- Click on the failed task
- Check the "Log" tab for error messages
- Common issues: missing dependencies, permission errors

---

## Quick Reference

| Action | How To |
|--------|--------|
| **Trigger DAG** | Click ▶️ Play button in DAG view |
| **View Logs** | Click task → "Log" tab |
| **See Status** | Check task color (green = success) |
| **Stop DAG** | Click ⏹️ Stop button (if running) |
| **Delete Run** | Click run → Delete button |

