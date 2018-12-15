from django.db import models
from cities.models import City

# Institution Model
class Institution(models.Model):
    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} ({})".format(self.name, self.city.name)
