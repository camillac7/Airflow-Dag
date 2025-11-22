# Where to See Your DAG Information

## 🌐 Airflow Web UI Locations

### 1. **DAGs List View** (Main Page)
**URL:** http://localhost:8080

**What you see:**
- List of all DAGs
- Toggle switches (ON/OFF) on the left
- Status indicators (colored circles)
- Last run time
- Next run time
- Run count
- Owner
- Tags

**How to access:**
- This is the default page when you log in
- Click "DAGs" in the top menu if you're on another page

---

### 2. **DAG Details Page** (Most Information)
**How to access:**
- Click on the DAG name `basic_dag` from the DAGs list

**What you see:**
- **Graph View**: Visual representation of your tasks and dependencies
- **Code**: The actual Python code of your DAG
- **Details**: Schedule, owner, tags, description
- **Runs**: History of all DAG runs
- **Trigger Button**: ▶️ Play button to manually trigger
- **Task Instances**: List of all task runs

**Tabs available:**
- **Graph**: Visual task flow (default)
- **Code**: Python source code
- **Details**: Metadata (schedule, owner, etc.)
- **Gantt**: Timeline view of runs
- **Task Duration**: Performance metrics
- **Task Tries**: Retry statistics
- **Landing Times**: When tasks started
- **Logs**: Centralized log view

---

### 3. **Task Details**
**How to access:**
- Click on any task (box) in the Graph view

**What you see:**
- Task ID
- Task type (BashOperator, PythonOperator, etc.)
- Status
- Duration
- Start/End times
- **Logs**: Click "Log" button to see task output
- Dependencies (upstream/downstream tasks)
- Task instance details

---

### 4. **DAG Run Details**
**How to access:**
- Click on a specific DAG run (from the "Runs" section or timeline)

**What you see:**
- Run ID
- Execution date
- Start/End time
- Duration
- State (success, failed, running, etc.)
- All tasks in that run
- Task statuses
- Configuration used

---

## 📊 Key Information Locations

### Schedule Information
- **Location**: DAG Details page → "Details" tab
- **Shows**: Schedule interval, start date, catchup settings

### Task Dependencies
- **Location**: DAG Details page → "Graph" tab
- **Shows**: Visual flow with arrows showing task order

### Logs
- **Location**: 
  - Task level: Click task → "Log" button
  - DAG level: DAG Details → "Logs" tab
- **Shows**: All output from your tasks

### Run History
- **Location**: DAG Details page → "Runs" section (right side)
- **Shows**: All past and current DAG runs

### Code
- **Location**: DAG Details page → "Code" tab
- **Shows**: The actual Python code of your DAG

---

## 🎯 Quick Navigation Guide

```
Airflow Web UI (http://localhost:8080)
│
├── DAGs (Main Menu)
│   └── List of all DAGs
│       └── Click "basic_dag"
│           ├── Graph Tab (Visual task flow)
│           ├── Code Tab (Python source)
│           ├── Details Tab (Schedule, metadata)
│           ├── Gantt Tab (Timeline)
│           └── Runs Section (Right side)
│               └── Click a run
│                   └── See all tasks in that run
│
└── Click any task box
    └── Task Details
        └── Log Button (See task output)
```

---

## 📝 What Information is Available

### DAG Level Info:
- ✅ DAG ID: `basic_dag`
- ✅ Description: "A very basic DAG example"
- ✅ Schedule: Daily (every 24 hours)
- ✅ Start Date: January 1, 2024
- ✅ Owner: airflow
- ✅ Tags: example, basic
- ✅ Catchup: False (won't backfill)
- ✅ Task count: 3 tasks
- ✅ Last run time
- ✅ Next run time
- ✅ Run history

### Task Level Info:
- ✅ Task ID (print_date, print_hello, print_goodbye)
- ✅ Task type (BashOperator, PythonOperator)
- ✅ Status (success, failed, running, etc.)
- ✅ Start/End times
- ✅ Duration
- ✅ Logs (actual output)
- ✅ Dependencies (which tasks run before/after)

---

## 🔍 Step-by-Step: View Your DAG Info

1. **Open Airflow UI**
   ```
   http://localhost:8080
   ```

2. **Find Your DAG**
   - Look for `basic_dag` in the list
   - You'll see: Status, Schedule, Last Run, etc.

3. **Click on `basic_dag`**
   - Opens the DAG details page

4. **Explore the Tabs:**
   - **Graph**: See your 3 tasks and how they connect
   - **Code**: See the Python code
   - **Details**: See schedule, owner, description

5. **View Task Info:**
   - Click any task box (print_date, print_hello, print_goodbye)
   - See task details
   - Click "Log" to see what it printed

6. **View Run History:**
   - Look at the "Runs" section on the right
   - Click any run to see all tasks in that run

---

## 💡 Pro Tips

- **Graph View** is the best way to understand task flow
- **Code Tab** shows exactly what your DAG does
- **Logs** show the actual output (date, "Hello from Airflow!", etc.)
- **Details Tab** has all the metadata (schedule, owner, etc.)
- **Runs Section** shows execution history

---

## 🚨 If You Don't See Your DAG

1. **Wait 30-60 seconds** - Scheduler needs time to scan
2. **Check for errors** - Red circle icon means there's an error
3. **Verify file location** - Should be in `~/airflow/dags/basic_dag.py`
4. **Check scheduler** - Make sure `airflow scheduler` is running
5. **Refresh the page** - Sometimes the UI needs a refresh

---

## 📍 Quick Reference

| What You Want to See | Where to Go |
|---------------------|-------------|
| **List of all DAGs** | Main page (DAGs menu) |
| **DAG structure/flow** | Click DAG → Graph tab |
| **DAG code** | Click DAG → Code tab |
| **Schedule info** | Click DAG → Details tab |
| **Task output/logs** | Click task → Log button |
| **Run history** | Click DAG → Runs section |
| **Task details** | Click task box in Graph view |

