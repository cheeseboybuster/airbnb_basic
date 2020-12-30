from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):
    
    """Review model definition"""
    
    review = models.TextField()
    accuracy = models.TextField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    checki_n = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete = models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.review}"  
    
    
    