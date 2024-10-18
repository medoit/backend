import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkasop.settings')
app = Celery('checkasop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'show_time': {
        'task': 'dashboard.tasks.show_time',
        'schedule': crontab(),
    },
    'load_sub_list': {
        'task': 'dashboard.tasks.load_sub_list',
        'schedule': crontab(minute='*/60'),
    },
    'load_snls_list': {
        'task': 'dashboard.tasks.load_snls_list',
        'schedule': crontab(minute='*/60'),
    },
}