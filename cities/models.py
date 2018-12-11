from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return "({}){}".format(self.code, self.name)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self):
        return "{}".format(self.name)
