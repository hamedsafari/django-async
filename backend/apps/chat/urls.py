from django.urls import path
from apps.chat.views import content

urlpatterns = [path("", content, name="content")]
