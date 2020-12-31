from django.db import models
from core import models as core_models

class Lists(core_models.TimeStampedModel):
    
    """Review model definition"""
    name = models.CharField(max_length=140)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name
    