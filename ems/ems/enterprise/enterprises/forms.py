#enterprise/forms.py
from django import forms
from .models import Claim, Warranty, Inspection

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claimDate']
        labels = {'claimDate': 'Date of Claim:'}


        # , 'warranty', 'status'
        # , 'warranty': 'Warranty Number:', 'status': 'Status:'

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