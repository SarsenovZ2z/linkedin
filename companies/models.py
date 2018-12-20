from django.db import models
from authentication.models import User
from cities.models import City

# Company Model
class Company(models.Model):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    COMPANY_TYPES = (
        ('OOO', 'Общество с ограниченной ответственностью'),
        ('PAO', 'Публичное акционерное общество'),
        ('AO', 'Акционерное общество'),
        ('UP', 'Учебное производство'),
        ('TOO', 'Товарищество с ограниченной ответственностью '),
        ('IP', 'Индивидуальный предприниматель'),
        ('AOO', 'Автономная организация образования'),
        ('ZAO', 'Закрытое акцтонерное общество'),
        ('OTHER', 'Другое'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, default='')
    short_name = models.CharField(max_length=255, default='')
    description = models.TextField(null=True, default='')
    short_description = models.TextField(null=True,default='')
    site = models.URLField(null=True,default='')
    company_type = models.CharField(
        max_length=255,
        choices = COMPANY_TYPES,
        default = "Индивидуальный предприниматель",
    )

    def __str__(self):
        return "{} {}".format(self.company_type, self.short_name);

# Post Model
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title);
