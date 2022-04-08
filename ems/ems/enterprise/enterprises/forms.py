#enterprise/forms.py
from django import forms
from .models import Claim, Warranty, Inspection, Inventory # ,Event
#from django.forms import ModelForm, DateInput

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claimDate', 'warranty', 'status', 'approvalDate']
        labels = {
            'claimDate': 'Date of Claim:',
            'warranty': 'Warranty Number:',
            'status': 'Status:',
            'approvalDate': 'Approval Date:'
            }
        

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['serialNumber', 'upcCode', 'name', 'dealership']
        labels = {
            'serialNumber': 'Serial Number:',
            'upcCode': 'UPC Code:',
            'name': 'Name:',
            'dealership': 'Dealership:'
            }

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['inspectionDate', 'inspectorName', 'dataEntryDate', 'claim']
        labels = {
            'inspectionDate': 'Date of Inspection:',
            'inspectorName': 'Inspector Name:',
            'dataEntryDate': 'Date of Data Entry:',
            'claim': 'Claim:'
        }

# copied from Hui Wen https://www.huiwenteo.com/normal/2018/07/29/django-calendar-ii.html
#class EventForm(ModelForm):
#  class Meta:
#    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
#    widgets = {
#      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#    }
#    fields = '__all__'

#  def __init__(self, *args, **kwargs):
#    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
#    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)