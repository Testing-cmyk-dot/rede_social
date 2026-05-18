from django.contrib import admin
from .models import Post, Comentario, Like

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Like)