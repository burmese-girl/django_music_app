from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
from django.http import FileResponse
from ..models import Track,Playlist
from rest_framework import viewsets
from ..serializers.music_serializers import *

def stream_track(request, track_id):
    track = Track.objects.get(id=track_id)
    response = FileResponse(open(track.file.path, 'rb'))
    return response

def create_playlist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        playlist = Playlist.objects.create(name=name, user=request.user)
        return redirect('playlist_detail', pk=playlist.pk)
    return render(request, 'music/create_playlist.html')

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
