from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('auth/', include('apps.admin_auth.urls')),
    path('teams/', include('apps.teams.urls')),
    path('players/', include('apps.players.urls')),
    path('matches/', include('apps.matches.urls')),
    path('teams.jsp', RedirectView.as_view(url='/teams/teams.jsp', permanent=False)),
    path('players.jsp', RedirectView.as_view(url='/players/players.jsp', permanent=False)),
    path('Matches.jsp', RedirectView.as_view(url='/matches/Matches.jsp', permanent=False)),
    path('adlogin.jsp', RedirectView.as_view(url='/auth/adlogin.jsp', permanent=False)),
    path('admindash.jsp', RedirectView.as_view(url='/teams/admindash.jsp', permanent=False)),
    path('adminPlayers.jsp', RedirectView.as_view(url='/players/adminPlayers.jsp', permanent=False)),
    path('adminMatches.jsp', RedirectView.as_view(url='/matches/adminMatches.jsp', permanent=False)),
    path('addTeam.jsp', RedirectView.as_view(url='/teams/addTeam.jsp', permanent=False)),
    path('addPlayer.jsp', RedirectView.as_view(url='/players/addPlayer.jsp', permanent=False)),
    path('addMatch.jsp', RedirectView.as_view(url='/matches/addMatch.jsp', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
