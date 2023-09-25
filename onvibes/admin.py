from django.contrib import admin
from .models import Song, Artist, Genre, Comment, Like

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Like)
