set -e

python manage.py makemigrations --merge --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn jcoet.wsgi:application --bind 0.0.0.0:8081 