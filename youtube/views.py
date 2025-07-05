from django.shortcuts import render
from django.views.generic import ListView
from .models import Videos
# Create your views here.
class VideosListView(ListView):
    model = Videos
    # template_name = "videos_list.html"