from datetime import datetime
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from louvor.models import Musica

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100, default=datetime.now)
    playlist_data = models.DateField(default=datetime.now, blank=True)
    playlist_musicas = models.ManyToManyField(Musica, through='PlaylistMusicas' ,blank=True)

    playlist_createdDate = models.DateField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete= models.SET_DEFAULT, default=1)
    def __str__(self) -> str:
        return self.playlist_name


class PlaylistMusicas(models.Model):
    musica = models.ForeignKey(Musica, on_delete = models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete = models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    order = models.IntegerField(default=1)

    class Meta:
      ordering = ['timestamp', 'order']