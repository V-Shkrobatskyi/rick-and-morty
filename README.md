# rick-and-morty-api

### How to run (on Windows):
- Create venv: `python -v venv .venv`
- Activate it: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Create new Postgres DB & User: `docker run --name rick_and_morty_postgres -e POSTGRES_PASSWORD=POSTGRES_PASSWORD -e POSTGRES_USER=POSTGRES_USER -e POSTGRES_DB=POSTGRES_DB -p 5432:POSTGRES_PORT -d postgres`
- Copy .env.sample to .env and populate with all required data
- Run migration: `python manage.py migrate`
- Run Redis Server: `docker run -d -p 6379:6379 redis`
- Run celery worker for tasks handling: `celery -A rick_and_morty_api worker -l info --pool=solo`
- Run celery beat task scheduling: `celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Create schedule for running sync in DB
- Run app: `python manage.py runserver`
