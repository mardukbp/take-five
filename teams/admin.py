from django.contrib import admin

from teams.forms import PlayerForm
from teams.models import Player, Team


@admin.register(Team)
class Teams(admin.ModelAdmin):
    pass


@admin.register(Player)
class Players(admin.ModelAdmin):
    form = PlayerForm
