from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model): # Post object for community board, foreign key on User.id to identify author and grant permissions to edit/delete
    title = models.CharField(max_length= 100)
    file = models.FileField(blank= True, null=True)
    content = models.TextField()
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)
    uploaded = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    upvote = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="liked")
    downvote = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="disliked")

    def __str__(self):
        return self.title

class Comment(models.Model): # comment object that is tied to a post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return '{} : {}'.format(self.user, self.content)