from django.db import models
from core import models as core_models

class Reservation(core_models.TimeStampedModel):
    """Reservation Model Defintion"""
    
    STATUS_PENDING = "pending"
    STATUS_COMFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_COMFIRMED, "confirmed"),
        (STATUS_CANCELED,"canceled"),
    )
    
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    guest = models.ForeignKey("users.USer", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()    
    
    def __str__(self): 
        return f"{self.room} - {self.check_in}"