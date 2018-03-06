from django.contrib import admin
from .models import Post,Comments, Editor, Profile

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Editor)
admin.site.register(Profile)
