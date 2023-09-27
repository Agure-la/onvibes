from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True, db_column='artist_id')
    name      = models.CharField(max_length=50, blank=False, null=False)
    location  = models.CharField(max_length=50, blank=False, null=False)
    city      = models.CharField(max_length=50, blank=False, null=False)


class Genre(models.Model):
    genre_id   = models.AutoField(primary_key=True, db_column='genre_id')
    genre_name = models.CharField(max_length=50, blank=False, null=False)




class Song(models.Model):
    song_id     = models.AutoField(primary_key=True, db_column='song_id')
    title       = models.CharField(max_length=200, blank=False, null=False)
    artist      = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres      = models.ManyToManyField(Genre)
    image       = models.ImageField(blank=True, null=True)
    audio_file  = models.FileField(blank=False, null=False)
    audio_link  = models.CharField(max_length=200, null=True, blank=True)
    duration    = models.CharField(max_length=20)
    upload_by   = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField();


class Comment(models.Model):
    comment_id    = models.AutoField(primary_key=True, db_column='comment_id')
    text         = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    song         = models.ForeignKey(Song, on_delete=models.CASCADE)


class Like(models.Model):
    like_id     = models.AutoField(primary_key=True, db_column='like_id')
    like_status = models.BooleanField()
    song        = models.ForeignKey(Song, on_delete=models.CASCADE)