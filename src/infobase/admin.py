from django.contrib import admin
from .models import Entry

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","user","timestamp"]
    list_filter = ["timestamp"]
    class Meta:
        model = Entry
admin.site.register(Entry, PostModelAdmin)