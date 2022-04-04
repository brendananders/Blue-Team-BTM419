from telnetlib import STATUS
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Dealership(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    phoneNumber = models.IntegerField()

class Inventory(models.Model):
    serialNumber = models.IntegerField()
    upcCode = models.IntegerField()
    name = models.CharField(max_length=30)
    dealership = models.ForeignKey(Dealership,on_delete=models.SET_NULL,null=True)

class Warranty(models.Model):
    inventory = models.ForeignKey(Inventory,on_delete=models.SET_NULL,null=True)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class Claim(models.Model):
    claimDate = models.DateField()
    warranty = models.ForeignKey(Warranty,on_delete=models.SET_NULL,null=True)
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
    approvalDate = models.DateField(blank=True, null=True)

class Inspection(models.Model):
    inspectorName = models.CharField(max_length=30) # stored because the form can be filled out on someone's behalf
    inspectionDate = models.DateField(blank=True, null=True)
    dataEntryDate = models.DateField()
<<<<<<< HEAD
    claim = models.ForeignKey(Claim,on_delete=models.SET_NULL,null=True) 
=======
    claim = models.ForeignKey(Claim,on_delete=models.SET_NULL,null=True)
>>>>>>> 213cd418cad7e3e606944e41bcf9e6d7a6caefce
