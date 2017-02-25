from __future__ import unicode_literals, absolute_import
import uuid
from django.db import models
from django.utils import timezone


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Team(Base):
    name = models.CharField(max_length=255, default=None)
    short_name = models.CharField(max_length=25, default=None)
    conference = models.ForeignKey('Conference')

    def __unicode__(self):
        return self.name


class Conference(Base):
    name = models.CharField(max_length=255, default=None)
    short_name = models.CharField(max_length=25, default=None)
    division = models.ForeignKey('Division')

    def __unicode__(self):
        return self.name

class Division(Base):
    name = models.CharField(max_length=255, default=None)
    short_name = models.CharField(max_length=25, default=None)
    league = models.ForeignKey('League')

    def __unicode__(self):
        return self.name

class League(Base):
    name = models.CharField(max_length=255, default=None)
    short_name = models.CharField(max_length=25, default=None)

    def __unicode__(self):
        return self.name


class PlayerPosition(Base):
    name = models.CharField(max_length=255, default=None)
    code = models.CharField(max_length=10, default=None)

    def __unicode__(self):
        return "({0}) {1}".format(self.code, self.name)


class Player(Base):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    height = models.IntegerField(default=0, help_text='In Inches')
    weight = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    team = models.ForeignKey('Team')
    position = models.ForeignKey('PlayerPosition')
    url = models.CharField(max_length=1024, default=None, null=True, blank=True)

    def __unicode__(self):
        return "#{0} {1} {2}".format(self.number, self.first_name, self.last_name)

class Game(Base):
    name = models.CharField(max_length=255, default=None)
    season = models.IntegerField(default=0)
    game_date = models.DateField(default=timezone.now)
    home_team = models.ForeignKey('Team', related_name='team_home')
    away_team = models.ForeignKey('Team', related_name='team_away')

    def __unicode__(self):
        return self.name

MAKE_THE_PLAY = (
    ('RUN', 'Run'),
    ('PASS', 'Pass'),
)

TRINARY_SCORE = (
    (0, '-'),
    (1, '+'),
)

class PlayType(Base):
    name = models.CharField(max_length=255, default=None)

    def __unicode__(self):
        return self.name

class PlayCall(Base):
    name = models.CharField(max_length=255, default=None)
    game = models.ForeignKey('Game')
    play_type = models.ForeignKey('PlayType')
    video_url = models.CharField(max_length=1024, default=None)
    make_the_play = models.CharField(max_length=4, choices=MAKE_THE_PLAY)
    ordinal = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class PlayCallPlayer(Base):
    play_call = models.ForeignKey('PlayCall')
    position = models.ForeignKey('PlayerPosition')
    player = models.ForeignKey('Player')
    comments = models.CharField(max_length=1024, default=None)
    tech = models.IntegerField(default=0, choices=TRINARY_SCORE)
    purs = models.IntegerField(default=0, choices=TRINARY_SCORE)

class PlayCallStat(Base):
    name = models.CharField(max_length=255, default=None)
    code = models.CharField(max_length=10, default=None)

    def __unicode__(self):
        return "({0}) {1}".format(self.code, self.name)



PLAYER_STAT_SCORES = (
    (0, ''),
    (1, '+'),
    (-1, '-'),
    (2, '++'),
    (-2, '--'),
    (3, '+++'),
    (-3, '---'),
    (4, '++++'),
    (-4, '----'),
    (5, '+++++'),
    (-5, '-----'),
    (6, '++++++'),
    (-6, '------'),
)



class PlayCallPlayerStat(Base):
    play_call_player = models.ForeignKey('PlayCallPlayer')
    play_call_stat = models.ForeignKey('PlayCallStat')
    score = models.IntegerField(default=0, choices=PLAYER_STAT_SCORES)


class Account(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True, default="")

   
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
