#!/usr/bin/env python3
"""
Create an admin user for Airflow 3.x
"""
import os
import sys

# Set AIRFLOW_HOME
os.environ['AIRFLOW_HOME'] = os.path.expanduser('~/airflow')

try:
    # Import Airflow components
    from airflow.configuration import conf
    from airflow.utils.db import init_db
    
    # Initialize database connection
    from airflow.utils.session import create_session
    
    with create_session() as session:
        # Try to import user model (varies by Airflow version)
        try:
            from flask_appbuilder.security.sqla.models import User as FABUser
            from flask_appbuilder.models.sqla.interface import SQLAInterface
            
            # Check if admin user exists
            admin_user = session.query(FABUser).filter(FABUser.username == 'admin').first()
            
            if admin_user:
                print("✅ Admin user already exists!")
                print(f"   Username: {admin_user.username}")
                print(f"   Email: {admin_user.email}")
                sys.exit(0)
            
            # Create admin user
            from werkzeug.security import generate_password_hash
            
            admin_user = FABUser()
            admin_user.username = 'admin'
            admin_user.email = 'admin@example.com'
            admin_user.first_name = 'Admin'
            admin_user.last_name = 'User'
            admin_user.active = True
            admin_user.password = generate_password_hash('admin')
            
            # Add roles
            from flask_appbuilder.security.sqla.models import Role
            admin_role = session.query(Role).filter(Role.name == 'Admin').first()
            if admin_role:
                admin_user.roles = [admin_role]
            
            session.add(admin_user)
            session.commit()
            
            print("✅ Admin user created successfully!")
            print("   Username: admin")
            print("   Password: admin")
            print("")
            print("You can now start Airflow and login with these credentials.")
            
        except ImportError as e:
            print(f"⚠️  Could not import user models: {e}")
            print("")
            print("Don't worry! Airflow standalone mode will create a user automatically.")
            print("When you run 'airflow standalone', watch the terminal output for credentials.")
            
except Exception as e:
    print(f"⚠️  Error: {e}")
    print("")
    print("Don't worry! You can still create a user through:")
    print("1. Airflow standalone mode (creates user automatically)")
    print("2. The web UI on first access")
    print("")
    print("Let's use option 1 - I'll guide you to start standalone mode.")

