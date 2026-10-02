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

app_name = 'matches'

urlpatterns = [
    path('public/', public_list, name='public_list'),
    path('Matches.jsp', public_list, name='public_list_jsp'),
    path('admin/', admin_list, name='admin_list'),
    path('adminMatches.jsp', admin_list, name='admin_list_jsp'),
    path('admin/add-page/', add_page, name='add_page'),
    path('addMatch.jsp', add_page, name='add_page_jsp'),
    path('admin/add/', add_action, name='add_action'),
    path('admin/edit/<int:match_id>/', edit_page, name='edit_page'),
    path('admin/update/', update_action, name='update_action'),
    path('admin/delete/<int:match_id>/', delete_action, name='delete_action'),
]
