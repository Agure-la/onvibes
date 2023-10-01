from django.urls import path
from .views import (
ArtistViewSet,
GenreViewSet,
SongViewSet,
LikeViewSet,
CommentViewSet,
)

app_name = 'onvibes'

urlpatterns = [

    # Artists
    path('artists/', ArtistViewSet.as_view({'get': 'list', 'post': 'create'}), name='artist-list'),
    path('artists/<int:artist_id>/', ArtistViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), nane='artist-detail'),

    # Genre
    path('genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre-list'),
    path('genres/<int:genre_id>/',
         GenreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         nane='genre-detail'),

    # Song
    path('songs/', SongViewSet.as_view({'get': 'list', 'post': 'create'}), name='song-list'),
    path('songs/<int:song_id>/',
         SongViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         nane='song-detail'),

    # Comment
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:comment_id>/',
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         nane='comment-detail'),

    # Like
    path('likes/', LikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='like-list'),
    path('likes/<int:like_id>/',
         LikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         nane='like-detail'),
]