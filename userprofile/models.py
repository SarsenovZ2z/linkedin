from django.db import models
from authentication.models import User
from cities.models import City
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    phone = models.IntegerField()
    skype = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        # data = {'city_id': self.city, 'phone': self.phone, 'skype': self.skype, 'date_of_birth': self.date_of_birth}

        return "{} {}".format(self.user.first_name, self.user.last_name)
