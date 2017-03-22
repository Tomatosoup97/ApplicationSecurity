from django.contrib import admin

from .models import Comment, Opinion


admin.site.register(Comment)
admin.site.register(Opinion)
