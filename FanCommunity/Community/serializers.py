from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Movie, FootballTeam, Post, Comment

# -------- User Serializer --------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

# -------- Movie Serializer --------
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'genre']

# -------- FootballTeam Serializer --------
class FootballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballTeam
        fields = ['id', 'name', 'country', 'founded_year']

# -------- Post Serializer --------
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'category']

# -------- Comment Serializer --------
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']

from .models import Like, FavoriteMovie, FavoriteTeam

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']

class FavoriteMovieSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = FavoriteMovie
        fields = ['id', 'user', 'movie']

class FavoriteTeamSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = FavoriteTeam
        fields = ['id', 'user', 'team']
