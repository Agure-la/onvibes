from django.shortcuts import get_object_or_404
from .models import Artist, Genre, Song, Like, Comment
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import SongSerializer, ArtistSerializer, CommentSerializer, LikeSerializer, GenreSerializer
from rest_framework.exceptions import NotFound


# Create your views here.

# Artist class Operations

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'artist_id'  # specify the primary key

    @action(detail=True, methods=['GET'])
    def retrieve_artist(self, request, artist_id=None):
        artist = get_object_or_404(Artist, artist_id=artist_id)
        serializer = self.get_serializer(artist)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_artist(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_artist(self, request, artist_id=None):
        artist = get_object_or_404(Artist, artist_id=artist_id)
        serializer = self.get_serializer(artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def delete_artist(self, request, artist_id=None):
        artist = get_object_or_404(Artist, artist_id=artist_id)
        artist.delete()
        return Response(status=204)


# genre class Operations

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'genre_id'  # specify the primary key

    @action(detail=True, methods=['GET'])
    def retrieve_genre(self, request, genre_id=None):
        genre = get_object_or_404(Genre, genre_id=genre_id)
        serializer = self.get_serializer(genre)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_genre(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_genre(self, request, genre_id=None):
        genre = get_object_or_404(Genre, genre_id=genre_id)
        serializer = self.get_serializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def delete_genre(self, request, genre_id=None):
        genre = get_object_or_404(Genre, genre_id=genre_id)
        genre.delete()
        return Response(status=204)


# Song Class Operations

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(detail=False, methods=['GET'])
    def list_songs(self, request):
        songs = self.get_queryset()
        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def retrieve_song(self, request, song_id=None):
        try:
            song = self.get_object()
        except Song.DoesNotExist:
            raise NotFound("Song Not Found")

        serializer = self.get_serializer(song)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_song(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_song(self, request, song_id=None):
        song = self.get_object()
        serializer = self.get_serializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def delete_song(self, request, song_id=None):
        song = self.get_object()
        song.delete()
        return Response(status=204)


# Comment Operations

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'comment_id'  # specify the primary key

    @action(detail=True, methods=['GET'])
    def retrieve_comment(self, request, comment_id=None):
        comment = get_object_or_404(Comment, comment_id=comment_id)
        serializer = self.get_serializer(comment)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_comment(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_comment(self, request, comment_id=None):
        comment = get_object_or_404(Comment, comment_id=comment_id)
        serializer = self.get_serializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def delete_comment(self, request, comment_id=None):
        comment = get_object_or_404(Comment, comment_id=comment_id)
        comment.delete()
        return Response(status=204)


# Like Operations

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'like_id'  # specify the primary key

    @action(detail=True, methods=['GET'])
    def retrieve_like(self, request, like_id=None):
        like = get_object_or_404(Like, like_id=like_id)
        serializer = self.get_serializer(like)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_like(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_like(self, request, like_id=None):
        like = get_object_or_404(Like, like_id=like_id)
        serializer = self.get_serializer(like, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def delete_like(self, request, like_id=None):
        like = get_object_or_404(Like, like_id=like_id)
        like.delete()
        return Response(status=204)
