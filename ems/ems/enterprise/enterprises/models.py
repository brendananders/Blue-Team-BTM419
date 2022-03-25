from telnetlib import STATUS
from django.db import models

# Create your models here.
class Dealership(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    phoneNumber = models.IntegerField(max_length=10)

class Inventory(models.Model):
    serialNumber = models.IntegerField(max_length=50)
    upcCode = models.IntegerField(max_length=12)
    name = models.CharField(max_length=30)
    dealership = models.ForeignKey(Dealership)

class Warranty(models.Model):
    inventory = models.ForeignKey(Inventory)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class Claim(models.Model):
    claimDate = models.DateField()
    warranty = models.ForeignKey(Warranty)
    STATUS_CHOICES = [
        ('AP', 'Approved'),
        ('RE', 'Rejected'),
        ('AC', 'Active'),
        ('PE', 'Pending')
    ]
    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = 'PE'
    ) 

class Inspection(models.Model):
    inspectorName = models.CharField(max_length=30) # stored because the form can be filled out on someone's behalf
    inspectionDate = models.DateField(blank=True, null=True)
    dataEntryDate = models.DateField()
    claim = models.ForeignKey(Claim)