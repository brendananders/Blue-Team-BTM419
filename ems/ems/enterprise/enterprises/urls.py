from django.contrib import admin 
from django.urls import path, include
from . import views

app_name = 'enterprises'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('claims/', views.claims, name='claims'),
    path('claimsIndex/', views.claimsIndex, name='claimsIndex'),
    path('newClaim/', views.newClaim, name='newClaim'),
    path('inventory/', views.inventory, name='inventory'),
    path('warranties/', views.warranties, name='warranties'),
    path('inspections/', views.inspections, name='inspections'),
    path('inspectionsIndex/', views.inspectionsIndex, name='inspectionsIndex'),
    path('newInspection/', views.newInspection, name='newInspection'),
    path('admin/', admin.site.urls),
    path('inspectionCalendar/', views.CalendarView.as_view(), name='inspectionCalendar'),
    path('event/', views.event, name='event'),
]
