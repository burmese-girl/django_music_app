from django.shortcuts import render
from ..models import Track

def track_list(request):
    tracks = Track.objects.all()  # Fetch all tracks from the database
    return render(request, 'music/music_tracks.html', {'tracks': tracks})


def index(request):
    tracks = Track.objects.all()  # Fetch all tracks from the database
    return render(request, 'music/music_tracks.html', {'tracks': tracks})
