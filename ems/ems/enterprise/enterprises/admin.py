from django.contrib import admin

# Register your models here.
from .models import Dealership, Inventory, Warranty, Claim, Inspection, Event

admin.site.register(Dealership)
admin.site.register(Inventory)
admin.site.register(Warranty)
admin.site.register(Claim)
admin.site.register(Inspection)
admin.site.register(Event)

