from django.shortcuts import render, render_to_response

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from audiolibrary.models import Song
from audiolibrary.serializers import SongSerializer


def get_songs(request):
    songs = Song.objects.all()
    return render_to_response('index.html', context={'songs': songs})

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
