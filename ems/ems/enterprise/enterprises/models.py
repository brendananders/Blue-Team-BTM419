from django.db import models

# Create your models here.
class Inventory(models.Model):
    serialNumber = models.IntegerField()
    upcCode = models.IntegerField(max_length=12)
    name = models.CharField()

class Warranty(models.Model):
    inventory = models.ForeignKey(Inventory)
    brand = models.CharField()

class Claim(models.Model):
    dateSubmitted = models.DateField()
    warranty = models.ForeignKey(Warranty)

class Inspection(models.Model):
    date = models.DateField()
    approvalDate = models.DateField(blank=True, null=True)
    claim = models.ForeignKey(Claim)




