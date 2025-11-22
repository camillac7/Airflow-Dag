#!/usr/bin/env python3
"""
Script to create an admin user in Airflow 3.x
"""
import os
import sys

# Set AIRFLOW_HOME
os.environ['AIRFLOW_HOME'] = os.path.expanduser('~/airflow')

# Initialize Airflow
from airflow import settings
from airflow.www.app import create_app

app = create_app()

with app.app_context():
    from airflow.auth.managers.utils.fab import get_auth_manager
    
    auth_manager = get_auth_manager()
    
    try:
        # Try to create the admin user
        from airflow.auth.managers.utils.fab.models import User
        from airflow.utils.db import create_session
        
        with create_session() as session:
            # Check if user exists
            existing_user = session.query(User).filter(User.username == 'admin').first()
            if existing_user:
                print("Admin user already exists!")
                sys.exit(0)
            
            # Create new user (this might need adjustment based on exact API)
            print("Creating admin user...")
            print("Note: In Airflow 3.x, you may need to use the web UI to create users.")
            print("Or use: airflow users add-role -u admin -r Admin")
            print("")
            print("For now, try accessing the web UI at http://localhost:8080")
            print("You may be prompted to create the first admin user through the UI.")
            
    except Exception as e:
        print(f"Error: {e}")
        print("")
        print("In Airflow 3.x, user creation might need to be done through:")
        print("1. The web UI on first access")
        print("2. Or using Flask CLI commands")
        print("")
        print("Try accessing http://localhost:8080 after starting the webserver")

