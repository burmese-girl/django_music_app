from django.contrib import admin
from .models import Artist,Album, Track, Playlist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-id']
    search_fields = []
    readonly_fields = []
    list_display = [f.name for f in Artist._meta.fields if not f.name == "id"]

class AlbumAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-id']
    search_fields = []
    readonly_fields = []
    list_display = [f.name for f in Album._meta.fields if not f.name == "id"]

class TrackAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-id']
    search_fields = []
    readonly_fields = []
    list_display = [f.name for f in Track._meta.fields if not f.name == "id"]

class PlaylistAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-id']
    search_fields = []
    readonly_fields = []
    list_display = [f.name for f in Playlist._meta.fields if not f.name == "id"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist,PlaylistAdmin)
