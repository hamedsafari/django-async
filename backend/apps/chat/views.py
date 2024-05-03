import random
import asyncio
from django.http import StreamingHttpResponse


async def content_stream():
    for char in "Hello World!":
        yield char
        await asyncio.sleep(random.random())


async def content(request):
    return StreamingHttpResponse(content_stream())
