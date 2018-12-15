from django.db import models

# Country Model
class Country(models.Model):
    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return "({}){}".format(self.code, self.name)


# City Model
class City(models.Model):
    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)
