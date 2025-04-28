from django.urls import path
from apps.chat.views import sync_content, async_content, render_template_nextjs_page, render_stream_nextjs_page

urlpatterns = [
    path("sync-content", sync_content, name="sync_content"),
    path("async-content", async_content, name="async_content"),
    path("template", render_template_nextjs_page, name="template"),
    path("nextjs", render_stream_nextjs_page, name="nextjs")
]
