from django.urls import path, re_path
from apps.chat.views import sync_content, async_content, nextjs_page_view

urlpatterns = [
    path("/sync-content", sync_content, name="sync_content"),
    path("/async-content", async_content, name="async_content"),
    re_path(r"dashboard/\d", nextjs_page_view, name="pdp"),
    path("dashboard", nextjs_page_view, name="plp"),
]
