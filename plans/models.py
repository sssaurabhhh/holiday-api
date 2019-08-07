from django.db import models

# Create your models here.


class Plans(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    status = models.BooleanField(default=True)



