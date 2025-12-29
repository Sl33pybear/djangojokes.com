from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from .models import Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke