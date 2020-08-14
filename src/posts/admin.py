from django.contrib import admin

from .models import Post, Comment
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "uploaded", "edited"]
    list_filter = ["uploaded"]
    search_fields = ["title","content"]
    class Meta:
        model = Post

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "uploaded"]
    list_filter = ["uploaded"]
    search_fields = ["user", "post"]

admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)