from django.urls import path

from .controllers.views import (
    add_action,
    add_page,
    admin_list,
    delete_action,
    edit_page,
    public_list,
    update_action,
)

app_name = 'players'

urlpatterns = [
    path('public/', public_list, name='public_list'),
    path('players.jsp', public_list, name='public_list_jsp'),
    path('admin/', admin_list, name='admin_list'),
    path('adminPlayers.jsp', admin_list, name='admin_list_jsp'),
    path('admin/add-page/', add_page, name='add_page'),
    path('addPlayer.jsp', add_page, name='add_page_jsp'),
    path('admin/add/', add_action, name='add_action'),
    path('admin/edit/<int:jersey_number>/<str:team_code>/', edit_page, name='edit_page'),
    path('admin/update/', update_action, name='update_action'),
    path('admin/delete/<int:jersey_number>/<str:team_code>/', delete_action, name='delete_action'),
]
