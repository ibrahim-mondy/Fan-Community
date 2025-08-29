from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch

from .models import Movie, FootballTeam, Post, Comment
from .serializers import (
    UserSerializer, MovieSerializer, FootballTeamSerializer,
    PostSerializer, CommentSerializer
)
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["list", "destroy", "update", "partial_update", "create"]:
            return [permissions.IsAdminUser()]

        return [permissions.IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff or getattr(request.user, "role", "") == "Admin" or request.user == instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({"detail": "Not allowed."}, status=status.HTTP_403_FORBIDDEN)


class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all().order_by("-release_date")
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        genre = self.request.query_params.get("genre")
        title = self.request.query_params.get("title")
        if genre:
            qs = qs.filter(genre__iexact=genre)
        if title:
            qs = qs.filter(title__icontains=title)
        return qs


class FootballTeamViewSet(viewsets.ModelViewSet):

    queryset = FootballTeam.objects.all().order_by("name")
    serializer_class = FootballTeamSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.query_params.get("country")
        name = self.request.query_params.get("name")
        if country:
            qs = qs.filter(country__iexact=country)
        if name:
            qs = qs.filter(name__icontains=name)
        return qs


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.select_related("user").order_by("-created_at")
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        # create
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        cat = self.request.query_params.get("category")
        user_id = self.request.query_params.get("user")
        if cat:
            qs = qs.filter(category__iexact=cat)
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs

    @action(detail=True, methods=["get"], permission_classes=[permissions.AllowAny])
    def comments(self, request, pk=None):

        post = self.get_object()
        comments = Comment.objects.select_related("user", "post").filter(post=post).order_by("created_at")
        data = CommentSerializer(comments, many=True).data
        return Response(data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "post").order_by("created_at")
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        # create
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.request.query_params.get("post")
        user_id = self.request.query_params.get("user")
        if post_id:
            qs = qs.filter(post_id=post_id)
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs
