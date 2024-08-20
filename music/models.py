from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to='tracks/')
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return f'{self.name} by {self.user.username}'
