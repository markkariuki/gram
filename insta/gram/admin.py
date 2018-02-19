from django.contrib import admin
from .models import Post,Comments, Editor

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Editor)
