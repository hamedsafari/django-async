from django.urls import path
from apps.chat.views import hello

urlpatterns = [path("", hello, name="hello")]
