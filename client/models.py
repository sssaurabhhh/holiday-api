from django.db import models
from django.db.models import signals
from django.dispatch import receiver

# from holiday.packages.models import Packages
# Create your models here.

__all__ = ['Leads',
           'Contacts',
           'Accounts',
           'Comments',
           'CustomerContacts'
           ]

class Leads(models.Model):
    fname = models.CharField(max_length=15,null=True,blank=True)
    lname = models.CharField(max_length=15,null=True,blank=True)
    # leadno = models.CharField(max_length=10,null=False,blank=False)
    emailid = models.EmailField(max_length=50,null=False,blank=True)
    address = models.TextField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    deleted = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.fname)

@receiver(signals.post_save, sender=Leads)
def create_contacts(sender, instance, created, **kwargs):
    print("Contacts created!!!!!!!!!")

class Contacts(models.Model):
    fname = models.CharField(max_length=15,null=False,blank=False)
    lname = models.CharField(max_length=15,null=False,blank=True)
    # contno = models.CharField(max_length=10,null=False,blank=False)
    emailid = models.EmailField(max_length=50,null=False,blank=False)
    address = models.TextField(max_length=100,null=True,blank=True)
    deleted = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Accounts(models.Model):
    fname = models.CharField(max_length=15, null=False, blank=False)
    lname = models.CharField(max_length=15, null=False, blank=True)
    # contno = models.CharField(max_length=10, null=False, blank=False)
    emailid = models.EmailField(max_length=50, null=False, blank=False)
    address = models.TextField(max_length=100, null=True, blank=True)
    # prodid = models.ForeignKey(Packages,on_delete=models.CASCADE())
    deleted = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Comments(models.Model):
    comments = models.TextField(max_length=200)
    entityid = models.ForeignKey(Leads,on_delete=models.CASCADE,related_name='comments')
    type = models.CharField(max_length=15)


class CustomerContacts(models.Model):
    contact_no = models.IntegerField(max_length=10)
    entityid = models.IntegerField(max_length=10)
    type = models.CharField(max_length=15)
    status = models.BooleanField(default=True)