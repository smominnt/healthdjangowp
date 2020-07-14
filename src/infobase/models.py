from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# Create your models here.
class Entry(models.Model): # dietary tracker data with foreign key on user id
    title = models.CharField(max_length=25)
    summary = models.CharField(blank=True, null=True, max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    c_amount = models.PositiveIntegerField(default=0)
    p_amount = models.PositiveIntegerField(default=0)
    quality = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

def make_entry(c_amount, p_amount, day): # create a temporary Entry object used to calculate daily totals
    tmp = Entry()
    tmp.c_amount = c_amount
    tmp.p_amount = p_amount
    tmp.timestamp = "Day: " + str(day)
    tmp.title = "Day totals"
    tmp.summary = ""
    tmp.quality = ""
    return tmp



