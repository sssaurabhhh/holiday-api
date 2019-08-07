from django.db import models

# Create your models here.

__all__ = [
    'Country',
    'Packages',
]


class Country(models.Model):
    cname = models.CharField(max_length=20, null=False, blank=False, unique=True)
    countrycode = models.CharField(max_length=8, null=False, blank=False, unique=True)
    status = models.BooleanField(default=True)


class Packages(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    packagecode = models.CharField(max_length=10, null=False, blank=False, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)