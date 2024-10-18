from celery import shared_task
from datetime import datetime
from .utils import load_sub, load_snls


@shared_task()
def show_time():
    print(datetime.now())

@shared_task()
def load_sub_list():
    print("Task: load_sub_list. Start. " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    load_sub()
    print("Task: load_sub_list. Finish. " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@shared_task()
def load_snls_list():
    print("Task: load_snls_list. Start. " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    load_snls()
    print("Task: load_snls_list. Finish. " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))