from django.urls import path
from .views import home

app_name = 'public'

urlpatterns = [
    path('', home, name='home'),
    path('main.jsp', home, name='home_jsp'),
]
