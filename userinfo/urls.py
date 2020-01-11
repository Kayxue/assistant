from django.urls import path
from .views import Userinfo

urlpatterns = [
    path('',Userinfo.as_view()),
]
