from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, MovieViewSet, FootballTeamViewSet,
    PostViewSet, CommentViewSet, LikeViewSet,
    FavoriteTeamViewSet, FavoriteMovieViewSet,
    signup, login, logout
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'teams', FootballTeamViewSet, basename='footballteam')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'favorite-teams', FavoriteTeamViewSet, basename='favoriteteam')
router.register(r'favorite-movies', FavoriteMovieViewSet, basename='favoritemovie')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
