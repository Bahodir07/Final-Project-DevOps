from celery import shared_task
import time

@shared_task
def example_task():
    time.sleep(10)
    return "Done"
