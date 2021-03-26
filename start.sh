# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Starting Server"
gunicorn --workers=5 --bind 0.0.0.0:8000 backend.wsgi
