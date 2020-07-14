from django.contrib import admin

# Register your models here.
from .models import Demo
from .models import Tdee
admin.site.register(Demo)
admin.site.register(Tdee)
