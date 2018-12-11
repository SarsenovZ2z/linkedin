from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    test = models.CharField(max_length=255, default='test')
