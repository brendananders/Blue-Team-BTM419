from telnetlib import STATUS
from django.db import models

# Create your models here.
class Dealership(models.Model):
    name = models.CharField()

class Inventory(models.Model):
    serialNumber = models.IntegerField()
    upcCode = models.IntegerField(max_length=12)
    name = models.CharField()
    dealership = models.ForeignKey(Dealership)

class Warranty(models.Model):
    inventory = models.ForeignKey(Inventory)
    brand = models.CharField()

class Claim(models.Model):
    dateSubmitted = models.DateField()
    warranty = models.ForeignKey(Warranty)
    STATUS_CHOICES = [
        ('AP', 'Approved'),
        ('RJ', 'Rejected'),
        ('AC', 'Active'),
        ('PE', 'Pending')
    ]
    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = 'PE'
    ) 

class Inspection(models.Model):
    inspectorName = models.CharField() # stored because the form can be filled out on someone's behalf
    date = models.DateField()
    approvalDate = models.DateField(blank=True, null=True)
    claim = models.ForeignKey(Claim)




