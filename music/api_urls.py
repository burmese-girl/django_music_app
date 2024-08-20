# from django.conf.urls import include, url
from django.urls import path, include,re_path
from .views.view_music import *
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

app_name = "music"

router = DefaultRouter()
router.register(r"stream_track", TrackViewSet, basename="stream_track")
router.register(r"play_list", PlaylistViewSet, basename="play_list")
router.register(r"artists", ArtistViewSet, basename="artists")
router.register(r"album", AlbumViewSet, basename="album")

urlpatterns = [

]

urlpatterns += router.urls