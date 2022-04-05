from django.urls import path
from . import views

app_name = 'enterprises'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('claims/', views.claims, name='claims'),
    path('claimsIndex/', views.claimsIndex, name='claimsIndex'),
    path('newClaim/', views.newClaim, name='newClaim'),
    path('warranties/', views.warranties, name='warranties'),
    path('inspections/', views.inspections, name='inspections'),
    path('inspectionsIndex/', views.inspectionsIndex, name='inspectionsIndex'),
]
