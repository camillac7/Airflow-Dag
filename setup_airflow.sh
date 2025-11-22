#!/bin/bash

# Setup script for Airflow on macOS with Python 3.13

echo "🚀 Setting up Apache Airflow..."
echo ""

# Step 1: Install Airflow
echo "📦 Step 1: Installing Apache Airflow 3.1.3..."
pip3 install 'apache-airflow==3.1.3' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.3/constraints-3.13.txt"

if [ $? -ne 0 ]; then
    echo "❌ Installation failed. Trying without constraints..."
    pip3 install 'apache-airflow==3.1.3'
fi

# Step 2: Set AIRFLOW_HOME
echo ""
echo "📁 Step 2: Setting up Airflow home directory..."
export AIRFLOW_HOME=~/airflow
echo "AIRFLOW_HOME set to: ~/airflow"

# Add to shell profile for permanent setting
if ! grep -q "export AIRFLOW_HOME=~/airflow" ~/.zshrc 2>/dev/null; then
    echo "" >> ~/.zshrc
    echo "# Airflow Configuration" >> ~/.zshrc
    echo "export AIRFLOW_HOME=~/airflow" >> ~/.zshrc
    echo "✅ Added AIRFLOW_HOME to ~/.zshrc"
fi

# Step 3: Initialize database
echo ""
echo "🗄️  Step 3: Initializing Airflow database..."
airflow db init

# Step 4: Create admin user
echo ""
echo "👤 Step 4: Creating admin user..."
echo "Username: admin"
echo "Password: admin"
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Step 5: Copy DAG file
echo ""
echo "📋 Step 5: Copying DAG file to Airflow..."
mkdir -p ~/airflow/dags
cp basic_dag.py ~/airflow/dags/
echo "✅ DAG file copied to ~/airflow/dags/"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Start the scheduler in one terminal:"
echo "   airflow scheduler"
echo ""
echo "2. Start the webserver in another terminal:"
echo "   airflow webserver --port 8080"
echo ""
echo "3. Open http://localhost:8080 in your browser"
echo "   Login with username: admin, password: admin"
echo ""

