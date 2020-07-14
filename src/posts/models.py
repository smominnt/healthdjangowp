from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model): # Post object for community board, foreign key on User.id to identify author and grant permissions to edit/delete
    title = models.CharField(max_length= 100)
    content = models.TextField()
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)
    uploaded = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title