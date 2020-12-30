from django.contrib import admin
from . import models


@admin.register(
    models.Review
)
class ReviewAdmin2(admin.ModelAdmin):

    """Review Admin Definition"""
    pass