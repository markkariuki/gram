from django.contrib import admin
from .models import Post,Comment, Editor, Profile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Editor)
admin.site.register(Profile)
