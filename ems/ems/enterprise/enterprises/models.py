from django.db import models

# Create your models here.
class Inventory(models.Model):
    serialNumber = models.IntegerField()
    upcCode = models.IntegerField(max_length=12)

class Warranty(models.Model):
    inventory = models.ForeignKey(Inventory)
    brand = models.CharField()

class Claim(models.Model):
    dateSubmitted = models.DateField()

class Inspection(models.Model):
    inspectorName = models.CharField()
    date = models.DateField()
    approvalDate = models.DateField(blank=True)
    claim = models.ForeignKey(Claim)




