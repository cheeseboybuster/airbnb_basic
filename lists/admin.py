from django.contrib import admin
from . import models

@admin.register(models.Lists)
class Listadmin(admin.ModelAdmin):
    pass

