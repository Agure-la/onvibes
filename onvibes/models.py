from django.db import models

# Create your models here.

class Song(models.Model):
    title       = models.TextField(blank=False, null=False)
    artist      = models.TextField(blank=False, null=False)
    image       = models.ImageField(blank=True, null=True)
    audio_file  = models.FileField(blank=False, null=False)
    audio_link  = models.CharField(max_length=200, null=True, blank=True)
    duration    = models.CharField(max_length=20)
    upload_by   = models.CharField(max_length=50)
    upload_date = models.DateTimeField()
    updated_at  = models.DateTimeField();




class Artist(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)



class Genre(models.Model):
    genre_name = models.CharField(max_length=50)


class Comment(models.Model):
    text         = models.TextField()
    comment_date = models.DateTimeField()


class Like(models.Model):
    like_status = models.BooleanField()