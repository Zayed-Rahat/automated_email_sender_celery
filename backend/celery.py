import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Asia/Dhaka'
 
app.conf.beat_schedule = {
    "every_sixty_seconds": {
        "task": "users.tasks.sixty_second_func",
        "schedule": timedelta(seconds=60),
    },
}
 
app.autodiscover_tasks()
 
 