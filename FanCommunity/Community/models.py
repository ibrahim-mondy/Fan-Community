from django.db import models
from django.contrib.auth.models import AbstractUser

# ***********************************************
# User Model
# ***********************************************


class User(AbstractUser):
    ROLE_CHOICES= [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

# ***********************************************
# Movie Model
# ***********************************************

class Movie(models.Model):
    title = models.CharField(max_length=225)
    descripton = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    
# ***********************************************
# FootballTeam Model
# ***********************************************

class FootballTeam(models.Model):
    name = models.CharField(max_length=225)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()

# *********************************************** 
# Post Model
# ***********************************************

class Post(models.Model):
    CATEGORY_CHOICES=[
        ('movie', 'movie'),
        ('football', 'football'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

# *********************************************** 
# Comment Model
# ***********************************************

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# ***********************************************
# Like Model
# ***********************************************

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    
    class Meta:
        unique_together = ('post', 'user')

# ***********************************************
# FavoriteTeam Model
# ***********************************************

class FavoriteTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_team')
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE, related_name='fans')
    
    class Meta:
        unique_together = ('user' , 'team')

# ***********************************************
# FavoriteMovie Model
# ***********************************************

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_movie')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='fans')
    
    class Meta:
        unique_together = ('user' , 'movie')