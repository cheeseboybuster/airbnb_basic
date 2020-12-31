from django.contrib import admin
from . import models

@admin.register(models.Conversation)
class Conversationadmin(admin.ModelAdmin):
    pass

@admin.register(models.Message)
class Messageadmin(admin.ModelAdmin):
    pass
