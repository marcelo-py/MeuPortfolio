from django import forms
from django.db import models
from django.utils import timezone


class Menssagens(models.Model):
    menssagem = models.TextField()
    usuario = models.CharField(max_length=15)
    data = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.usuario


class VideoSugestao(models.Model):
    link_video = models.CharField(max_length=100, verbose_name='link')
    usuario_video = models.CharField(max_length=15, verbose_name='usuario')

    def __str__(self):
        return self.link_video


class SobreMim(models.Model):
    sobre = models.TextField()
    projetos = models.TextField()
    mostrar = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sobre

