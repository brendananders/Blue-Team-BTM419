import django_filters

from .models import *

class InspectionFilter(django_filters.FilterSet):
    class Meta:
        model = Inspection
        fields = '__all__'





