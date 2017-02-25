from __future__ import absolute_import, unicode_literals

import nested_admin
from django.contrib import admin
from nested_admin.nested import NestedModelAdmin

from .models import *



@admin.register(Account)
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    model = Player


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    model = Conference

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    model = Division

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    model = League

@admin.register(PlayType)
class PlayTypeAdmin(admin.ModelAdmin):
    model = PlayType


@admin.register(PlayerPosition)
class PlayerPositionAdmin(admin.ModelAdmin):
    model = PlayerPosition


@admin.register(PlayCallStat)
class PlayCallStatAdmin(admin.ModelAdmin):
    model = PlayCallStat


class PlayCallPlayerStatInline(nested_admin.NestedStackedInline):
    model = PlayCallPlayerStat
    extra = 1

class PlayCallPlayerInline(nested_admin.NestedStackedInline):
    model = PlayCallPlayer
    inlines = (PlayCallPlayerStatInline,)
    extra = 1


@admin.register(PlayCall)
class PlayCallAdmin(NestedModelAdmin):
    model = PlayCall
    inlines = (PlayCallPlayerInline, )


