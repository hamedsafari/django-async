import time
import random
import asyncio
from asgiref.sync import sync_to_async
from django.http import StreamingHttpResponse

MESSAGE = "This is a sample message.\n"


def sync_content_stream():
    for char in MESSAGE:
        yield char
        time.sleep(random.random())


def sync_content(request):
    return StreamingHttpResponse(sync_content_stream())


def sync_wait():
    time.sleep(random.random())


async def async_content_stream_with_sync_code_inside():
    for char in MESSAGE:
        yield char
        await sync_to_async(sync_wait)()


async def async_content_stream():
    for char in MESSAGE:
        yield char
        await asyncio.sleep(random.random())


async def async_content(request):
    return StreamingHttpResponse(async_content_stream())


# async def nextjs_page_view(request):
#     from django_nextjs.render import render_nextjs_page
#
#     return await render_nextjs_page(request, "django_nextjs/document_base.html")


async def nextjs_page_view(request):
    from django_nextjs.render import stream_nextjs_page

    return await stream_nextjs_page(request, "django_nextjs/document_base.html")
