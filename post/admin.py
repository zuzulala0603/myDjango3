from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'title',
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'content',
    )



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)