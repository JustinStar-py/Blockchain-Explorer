import asyncio
from os import name
from celery import shared_task
import time,requests,asyncio
from .utils import send_request

@shared_task(name="send_req")
def get_data():
    return asyncio.run(send_request())