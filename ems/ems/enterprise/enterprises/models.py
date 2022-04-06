from telnetlib import STATUS
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Dealership(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    phoneNumber = models.IntegerField()

    def __str__(self):
        return(str(self.name))

class Inventory(models.Model):
    serialNumber = models.IntegerField()
    upcCode = models.IntegerField()
    name = models.CharField(max_length=30)
    dealership = models.ForeignKey(Dealership,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return(str(self.serialNumber))

class Warranty(models.Model):
    inventory = models.ForeignKey(Inventory,on_delete=models.SET_NULL,null=True)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return(str(self.pk))

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

    def __str__(self):
        return(str(self.pk))
    

class Inspection(models.Model):
    inspectorName = models.CharField(max_length=30) # stored because the form can be filled out on someone's behalf
    inspectionDate = models.DateField(blank=True, null=True)
    dataEntryDate = models.DateField()
    claim = models.ForeignKey(Claim,on_delete=models.SET_NULL,null=True) 
        
    def __str__(self):
        return(str(self.pk))  

# copied from Hui Wenteo https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
