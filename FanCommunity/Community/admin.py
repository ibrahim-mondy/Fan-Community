from django.contrib import admin
from .models import User, Movie, FootballTeam, Post, Comment, Like, FavoriteTeam, FavoriteMovie

# Register your models here.

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(FootballTeam)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(FavoriteTeam)
admin.site.register(FavoriteMovie)