from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    MovieViewSet,
    FootballTeamViewSet,
    PostViewSet,
    CommentViewSet
)


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'teams', FootballTeamViewSet, basename='footballteam')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUpView, LogoutView

urlpatterns = [
    # --- Auth Routes ---
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('auth/login/', obtain_auth_token, name='login'),  
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
