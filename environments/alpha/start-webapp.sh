#!/bin/bash
set -e

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Starting ASGI server with uvicorn..."

exec uvicorn webapp.config.asgi:application --host 0.0.0.0 --port ${PORT}
