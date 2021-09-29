import os

from celery import Celery
from django.conf import settings

from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'development_test.settings')

app = Celery('development_test')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat settings times are UTC, 6 hours difference (8am) and day of the week set to be Mondays (1)
app.conf.beat_schedule = {
    'send-weekly-mail': {
        'task': 'email_celery.tasks.send_mail_func',
        'schedule': crontab(hour=14, minute=0, day_of_week=1),

    }
}


# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
