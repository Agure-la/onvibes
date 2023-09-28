from rest_framework import serializers
from .models import Song, Genre, Like, Artist, Comment


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # Serialize genres as nested objects
    artist = ArtistSerializer()  # Nested serializer for the Artist relationship
    comments = CommentSerializer(many=True, read_only=True)  # Serialize comments as nested objects
    likes = LikeSerializer(many=True, read_only=True)  # Serialize likes as nested objects

    class Meta:
        model = Song
        fields = '__all__'
