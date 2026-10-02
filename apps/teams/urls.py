from django.urls import path

from .controllers.views import (
    add_team_action,
    add_team_page,
    admin_dashboard,
    delete_team_action,
    public_list,
    update_team_action,
    update_team_page,
)

app_name = 'teams'

urlpatterns = [
    path('public/', public_list, name='public_list'),
    path('teams.jsp', public_list, name='public_list_jsp'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('admindash.jsp', admin_dashboard, name='admin_dashboard_jsp'),
    path('admin/add/', add_team_action, name='add_team_action'),
    path('admin/add-page/', add_team_page, name='add_team_page'),
    path('addTeam.jsp', add_team_page, name='add_team_page_jsp'),
    path('admin/edit/<str:code>/', update_team_page, name='update_team_page'),
    path('admin/update/', update_team_action, name='update_team_action'),
    path('admin/delete/<str:code>/', delete_team_action, name='delete_team_action'),
]
