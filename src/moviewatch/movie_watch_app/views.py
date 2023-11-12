from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
#from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView 
from . models import Movie
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

# Create your views here.



class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movie_form.html'
    fields = ['title', 'description', 'year_released', 'watched']
    success_url = reverse_lazy('movie_list')


def index(request):
    return render(request, 'index.html')

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movie'

# class MovieCreateView(CreateView):
#     model = Movie
#     fields = ['title', 'description', 'year_released', 'watched']
#     template_name = 'movie_form.html'
#     success_url = reverse_lazy('movie_list')

# class MovieUpdateView(UpdateView):
#     model = Movie
#     fields = ['title', 'description', 'year_released', 'watched']
#     template_name = 'movie_form.html'
#     success_url = reverse_lazy('movie_list')

# class MovieDetailView(DetailView):
#     model = Movie
#     template_name = 'movie_detail.html'

# class MovieDeleteView(DeleteView):
#     model = Movie
#     template_name = 'movie_confirm_delete.html'
#     success_url = reverse_lazy('movie_list')
