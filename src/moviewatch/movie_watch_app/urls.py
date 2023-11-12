
#from .views import MovieListView
from django.contrib import admin
from django.urls import path
from . views import MovieCreateView, MovieListView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', MovieListView.as_view(), name='movie_list'),
    # path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('add/', MovieCreateView.as_view(), name='movie_add'),
    # path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    # path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),

]
