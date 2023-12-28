from django.contrib import admin
from .models import usermodel
from .models import house

admin.site.register(usermodel)
admin.site.register(house)

# Register your models here.
