# Landing
Landing page


export DJANGO_SETTINGS_MODULE=landing.settings
export PYTHONPATH=/workspace/Landing


echo "OPENAI_API_KEY=" >> .env

cd /workspace/Landing/landing

python3 manage.py runserver

python3 manage.py collectstatic