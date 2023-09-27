from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Artist, Genre, Song, Like, Comment
from .forms import ArtistForm, GenreForm, SongForm, LikeForm, CommentForm


# Create your views here.

# Artist class Operations

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artist'


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artist_form.html'
    success_url = 'artist-list'


class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artist_form.html'
    success_url = 'artist-list'


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'


class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artist_confirm_delete.html'
    success_url = 'artist_list'


# genre class Operations

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'
    context_object_name = 'genre'


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre_form.html'
    success_url = 'genre_list'  # Redirect to the genre list view


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre_form.html'
    success_url = 'genre_list'  # Redirect to the genre list view


class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'
    context_object_name = 'genres'  # Optional: You can customize the context variable name


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'genre_confirm_delete.html'
    success_url = 'genre_list'


# Song Class Operations

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'


class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'song_form.html'
    success_url = 'song_list'  # Redirect to the song list view


class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'song_form.html'
    success_url = 'song_list'  # Redirect to the song list view


class SongListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'  # Optional: You can customize the context variable name


class SongDeleteView(DeleteView):
    model = Song
    template_name = 'song_confirm_delete.html'
    success_url = 'song_list'


# Comment Operations

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    context_object_name = 'comment'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = 'comment_list'  # Redirect to the comment list view


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = 'comment_list'  # Redirect to the comment list view


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'comments'  # Optional: You can customize the context variable name


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    success_url = 'comment_list'


# Like Operations

class LikeDetailView(DetailView):
    model = Like
    template_name = 'like_detail.html'
    context_object_name = 'like'


class LikeCreateView(CreateView):
    model = Like
    form_class = LikeForm
    template_name = 'like_form.html'
    success_url = 'like_list'  # Redirect to the like list view


class LikeUpdateView(UpdateView):
    model = Like
    form_class = LikeForm
    template_name = 'like_form.html'
    success_url = 'like_list'  # Redirect to the like list view


class LikeListView(ListView):
    model = Like
    template_name = 'like_list.html'
    context_object_name = 'likes'  # Optional: You can customize the context variable name


class LikeDeleteView(DeleteView):
    model = Like
    template_name = 'like_confirm_delete.html'
    success_url = 'like_list'
