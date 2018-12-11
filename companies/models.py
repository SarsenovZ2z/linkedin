from django.db import models
from authentication import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    
