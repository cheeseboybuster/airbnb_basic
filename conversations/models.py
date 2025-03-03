from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):
    
    """Conversation model definition"""
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)

class Message(core_models.TimeStampedModel):
    
    """Conversation model definition"""
    
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    Conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} syas: {self.message}"