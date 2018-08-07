from django.db import models


class PhotoItem(models.Model):
    image = models.ImageField(upload_to='upload/')


class VideoItem(models.Model):
    src = models.CharField(max_length=500)


class QuickPhotoItem(models.Model):
    image = models.ImageField(upload_to='upload/')
