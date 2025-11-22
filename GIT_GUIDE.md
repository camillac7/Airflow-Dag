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

### Option A: Initialize and Push to Existing GitHub Repo

```bash
# 1. Initialize git repository
git init

# 2. Add all files (respects .gitignore)
git add .

# 3. Make initial commit
git commit -m "Initial commit: Basic Airflow DAG"

# 4. Link to your GitHub repository
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# 5. Verify remote
git remote -v

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

### Option B: Create New GitHub Repo First

1. Go to GitHub.com
2. Click "New Repository"
3. **DON'T** initialize with README (since you already have files)
4. Copy the repository URL
5. Then run:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

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

