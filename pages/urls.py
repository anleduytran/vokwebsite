from django.urls import path
from . import views


urlpatterns = [
    path('vokrecords', views.index,name="index"),
    path('song', views.song, name="song"),

]
