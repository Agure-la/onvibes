from django import forms
from .models import Artist, Song, Comment, Like, Genre

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'city', 'location']



class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title','artist', 'genre', 'image', 'audio_file', 'upload_by']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'song']

class LikeForm(forms.ModelForm):
    class Meta:
        fields = ['like_status', 'song']