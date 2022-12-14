from django.db import models
from datetime import datetime
from artista.models import Artista
from django.contrib.auth.models import User


class Musica(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_DEFAULT, default=1)
    titulo_musica = models.CharField(max_length=200)
    nome_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    lyrics = models.TextField()
    chords = models.TextField(blank=True)
    data_musica = models.DateField(default=datetime.now, blank=True)

    def estrofes(self)-> str:
      estrofes = self.lyrics.split("£")
      return estrofes
      

    


