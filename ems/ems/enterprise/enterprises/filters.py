import django_filters

from .models import *

class InspectionFilter(django_filters.FilterSet):
    class Meta:
        model = Inspection
        fields = '__all__'

class ClaimsFilter(django_filters.FilterSet):
    class Meta:
        model = Claim
        fields = '__all__'

class WarrantiesFilter(django_filters.FilterSet):
    class Meta:
        model = Warranty
        fields = '__all__'

class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields = '__all__'


