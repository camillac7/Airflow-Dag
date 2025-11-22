# Git Repository Check & Setup Guide

## Current Status

This directory (`/Users/camillacalle/Downloads/DAGS`) is **NOT** a git repository.

---

## How to Check if a Directory is Linked to GitHub

### 1. Check if it's a Git Repository

```bash
cd /Users/camillacalle/Downloads/DAGS
git status
```

- If you see branch/status info → It's a git repo
- If you see "not a git repository" → It's not initialized

### 2. Check for GitHub Remote

```bash
git remote -v
```

This shows:
- `origin` - usually your GitHub repo
- Other remotes (if any)

**Example output if linked:**
```
origin  https://github.com/username/repo-name.git (fetch)
origin  https://github.com/username/repo-name.git (push)
```

### 3. Check Remote URL

```bash
git config --get remote.origin.url
```

Shows the exact GitHub repository URL.

### 4. Check All Git Configuration

```bash
git config --list --local
```

Shows all git settings for this repository.

---

## If You Want to Link This to GitHub

### ⚠️ Important: You MUST Create the GitHub Repository First!

**Yes, you need to create the repository on GitHub's website (or via GitHub CLI) BEFORE you can link your local code to it.**

---

### Step-by-Step Process:

#### Step 1: Create GitHub Repository (On GitHub Website)

1. Go to **https://github.com** and log in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Choose a repository name (e.g., `airflow-dags`)
4. **Important:** Choose **"Public"** or **"Private"** (private recommended for DAGs)
5. **DO NOT** initialize with README, .gitignore, or license (since you already have files)
6. Click **"Create repository"**

**GitHub will show you the repository URL** (something like `https://github.com/YOUR-USERNAME/REPO-NAME.git`)

#### Step 2: Link Your Local Code to GitHub

**Now run these commands in your terminal:**

```bash
# 1. Make sure you're in the right directory
cd /Users/camillacalle/Downloads/DAGS

# 2. Initialize git repository (if not already done)
git init

# 3. Add all files (respects .gitignore - won't add credentials!)
git add .

# 4. Make initial commit
git commit -m "Initial commit: Basic Airflow DAG"

# 5. Link to your GitHub repository (use the URL from Step 1)
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# 6. Verify remote was added correctly
git remote -v

# 7. Push to GitHub
git branch -M main
git push -u origin main
```

---

### Alternative: Using GitHub CLI (If You Have It Installed)

If you have `gh` (GitHub CLI) installed, you can create the repo from command line:

```bash
# Create repo on GitHub and link automatically
gh repo create airflow-dags --private --source=. --remote=origin --push
```

But **most people use the website method** (Step 1 above).

---

## Security Reminder

✅ Your `.gitignore` file is already configured to exclude:
- `YOUR_CREDENTIALS.txt`
- Password files
- Airflow database files
- Other sensitive data

Always check what you're committing:
```bash
git status
git diff
```

---

## Quick Check Commands Reference

| Command | Purpose |
|---------|---------|
| `git status` | Check if repo exists and current state |
| `git remote -v` | List all remotes (GitHub links) |
| `git config --get remote.origin.url` | Get GitHub URL |
| `git log --oneline` | See commit history |
| `git branch -a` | List all branches (local & remote) |

---

## Check Parent Directories

If you want to check if a parent directory is a git repository:

```bash
# Check parent directory
cd ..
git status

# Or check home directory
cd ~
git status
```

