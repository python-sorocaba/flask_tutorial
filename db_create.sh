#!/bin/bash

# Generate migrations directories and files
python manage.py db init
# Generate migration to model
python manage.py db migrate
# Show sql script
python manage.py db upgrade --sql
# Run online sql
python manage.py db upgrade
# Move database to project tvseries
mv tvseries.sqlite3 tvseries

