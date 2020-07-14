from django.urls import path
from .views import (
    posts_view,
    posts_create_view,
    posts_detail_view,
    posts_edit_view,
    posts_delete_view
)


app_name = 'post'
urlpatterns = [
    path('posts/', posts_view, name="posthome"),
    path('posts/<int:id>', posts_detail_view, name="postdetail"),
    path('posts/write/', posts_create_view, name="postcreate"),
    path('posts/edit/<int:id>', posts_edit_view, name="postedit"),
    path('posts/delete/<int:id>', posts_delete_view, name="postdelete"),
]
