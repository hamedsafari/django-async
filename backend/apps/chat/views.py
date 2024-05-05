import time
import random
import asyncio
from django.http import StreamingHttpResponse

MESSAGE = "This is a sample message.\n"


def sync_content_stream():
    for char in MESSAGE:
        yield char
        time.sleep(random.random())


def sync_content(request):
    return StreamingHttpResponse(sync_content_stream())


async def async_content_stream():
    for char in MESSAGE:
        yield char
        await asyncio.sleep(random.random())


async def async_content(request):
    return StreamingHttpResponse(async_content_stream())
