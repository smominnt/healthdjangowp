from django.db import models
from django.conf import settings

# Create your models here.
class Demo(models.Model):
    demo_title = models.CharField(max_length=200)
    demo_description = models.CharField(max_length=200)
    def __str__(self):
        return self.demo_title

class Tdee(models.Model):   # create model for tdee calculator
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    bmr = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    feet = models.PositiveIntegerField(default=0)
    inches = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    sex = models.BooleanField()