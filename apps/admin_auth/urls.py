from django.urls import path
from .controllers.views import login_view, logout_view

app_name = 'admin_auth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('adlogin.jsp', login_view, name='login_jsp'),
    path('adminloginservlet', login_view, name='login_servlet'),
]
