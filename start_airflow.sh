#!/bin/bash
# Script to start Airflow standalone and show credentials

export AIRFLOW_HOME=~/airflow

echo "🚀 Starting Airflow standalone..."
echo "📝 Watch for the admin credentials below!"
echo ""
echo "When you see credentials, you can:"
echo "1. Copy the username and password"
echo "2. Open http://localhost:8080 in your browser"
echo "3. Login with those credentials"
echo ""
echo "Press Ctrl+C to stop Airflow"
echo ""
echo "--- Starting Airflow ---"
echo ""

# Start standalone (will show credentials in output)
airflow standalone

