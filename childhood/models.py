__author__ = 'Abdullah'

from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Videos(models.Model):
    # row_id=models.AutoField(primary_key=True)
    video_id=models.AutoField(primary_key=True)
    video_name=models.CharField(max_length=100)
    video_path=models.FileField('childhood/media')
