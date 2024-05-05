from django.urls import path
from apps.chat.views import sync_content, async_content

urlpatterns = [
    path("sync-content", sync_content, name="sync_content"),
    path("async-content", async_content, name="async_content")
]
