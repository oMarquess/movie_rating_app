
from .views import MovieListView
from django.contrib import admin
from django.urls import path
from . views import MovieListView, index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('list', MovieListView.as_view(), name='movie_list'),

]
