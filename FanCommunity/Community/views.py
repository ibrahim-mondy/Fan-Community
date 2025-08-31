from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .models import Movie, FootballTeam, Post, Comment, Like, FavoriteMovie, FavoriteTeam
from .serializers import (
    UserSerializer, MovieSerializer, FootballTeamSerializer,
    PostSerializer, CommentSerializer
)
from .serializers import (
    LikeSerializer, FavoriteMovieSerializer, FavoriteTeamSerializer
)

User = get_user_model()


# ----------------- User -----------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# ----------------- Movie -----------------
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]


# ----------------- FootballTeam -----------------
class FootballTeamViewSet(viewsets.ModelViewSet):
    queryset = FootballTeam.objects.all()
    serializer_class = FootballTeamSerializer
    permission_classes = [AllowAny]


# ----------------- Post -----------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


# ----------------- Comment -----------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]


# ----------------- Like -----------------
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]

class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer
    permission_classes = [AllowAny]

class FavoriteTeamViewSet(viewsets.ModelViewSet):
    queryset = FavoriteTeam.objects.all()
    serializer_class = FavoriteTeamSerializer
    permission_classes = [AllowAny]


# ----------------- Signup API -----------------
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'GET':
        return Response({"message": "Use POST to create a user"})

    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created", "username": user.username}, status=201)


# ----------------- Login API -----------------
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def login(request):
    return Response({"message": "Login not required in this mode"}, status=200)


# ----------------- Logout API -----------------
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def logout(request):
    return Response({"message": "Logout not required in this mode"}, status=200)
