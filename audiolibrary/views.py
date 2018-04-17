from django.shortcuts import render, render_to_response

# Create your views here.
from audiolibrary.models import Song


def get_songs(request):
    songs = Song.objects.all()
    return render_to_response('index.html', context={'songs': songs})