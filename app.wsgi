import sys
import os

# Add the app's directory to the PYTHONPATH
sys.path.insert(0, "/var/www/wsgi/timesheet-backend")

# Activate the virtualenv
activate_this = os.path.join('/var/www/wsgi/timesheet-backend/venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application