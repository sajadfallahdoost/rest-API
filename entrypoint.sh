#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create superuser
echo "Creating superuser..."
python manage.py create_superuser

# Start Gunicorn server (if using Gunicorn, otherwise use runserver for development)
# gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000

# Start Django's development server (use for development only)
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000