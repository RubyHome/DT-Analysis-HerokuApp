from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^games/$', views.games, name="games"),
    url(r'^grades/$', views.grades, name="grades"),
    url(r'^players/$', views.players, name="players"),
]