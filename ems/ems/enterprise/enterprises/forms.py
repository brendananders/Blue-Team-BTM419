#enterprise/forms.py
from django import forms
from .models import Claim, Warranty

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claimDate']
        labels = {'claimDate': 'Date of Claim:'}


        # , 'warranty', 'status'
        # , 'warranty': 'Warranty Number:', 'status': 'Status:'