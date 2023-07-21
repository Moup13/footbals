from django.db import models

# Create your models here.
from django.urls import reverse


class Football(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128, null=True, blank=True)
    description = models.CharField(verbose_name='Описание',max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='football')
    url = models.URLField(max_length=1130, unique=True,default = '')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Футбол'
        verbose_name_plural = 'Футбол'




class MinyFootball(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128, null=True, blank=True)
    description = models.CharField(verbose_name='Описание',max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='miny_football')
    url = models.URLField(max_length=1130, unique=True, default = '')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мини-футбол'
        verbose_name_plural = 'Мини-футбол'



