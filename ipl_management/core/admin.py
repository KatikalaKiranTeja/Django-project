from django.contrib import admin

# Register your models here.

from .models import Team, Player, Match, PointsTable

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(PointsTable)