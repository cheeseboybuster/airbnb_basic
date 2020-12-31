from django.contrib import admin
from . import models


@admin.register(
    models.Reservation
)
class Reservationadmin(admin.ModelAdmin):
    
    """Reservation admin definition"""
    
    pass
