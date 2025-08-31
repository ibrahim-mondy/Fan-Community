from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserViewSet, MovieViewSet, FootballTeamViewSet,
    PostViewSet, CommentViewSet,
    signup, login, logout
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'teams', FootballTeamViewSet, basename='footballteam')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication routes
    path('api/auth/', include('authentication.urls')),

    # Core app routes
    path('api/movies/', include('movies.urls')),
    path('api/football-teams/', include('football.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/favorite-teams/', include('favorites.urls_team')),
    path('api/favorite-movies/', include('favorites.urls_movie')),
]

