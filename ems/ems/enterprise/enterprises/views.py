from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ClaimForm, InspectionForm, EventForm
from django.contrib.auth.decorators import login_required
from .filters import InspectionFilter
# copied from Hui Wenteo https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
from datetime import datetime, timedelta, date
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar
from django.urls import reverse
import calendar




# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'enterprises/index.html')

def inventory(request):
    """Inventory Page"""
    return render(request, 'enterprises/inventory.html')

def claims(request):
    """claims main menu"""
    return render(request, 'enterprises/claims.html')

@login_required
def claimsIndex(request):
    """claims index"""
    claimsList=Claim.objects.order_by('claimDate')
    context={'claims':claimsList}
    return render(request, 'enterprises/claimsIndex.html', context)
    
@login_required
def newClaim(request):
    """Add a new claim."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClaimForm()
    else:
        # POST data submitted; process data.
        form = ClaimForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprises:claimsIndex')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'enterprises/newClaim.html', context)

@login_required
def warranties(request):
    """claims index"""
    warrantiesList=Warranty.objects.order_by('inventory')
    context={'warranties':warrantiesList}
    return render(request, 'enterprises/warranties.html', context)

def inspections(request):
    """inspections main menu"""
    return render(request, 'enterprises/inspections.html')

@login_required
def inspectionsIndex(request):
    """inspections index"""
    inspectionsList=Inspection.objects.order_by('inspectionDate')
    context={'inspections':inspectionsList}
    return render(request, 'enterprises/inspectionsIndex.html', context)

@login_required
def newInspection(request):
    """Add a new inspection."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = InspectionForm()
    else:
        # POST data submitted; process data.
        form = InspectionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprises:inspectionsIndex')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'enterprises/newInspection.html', context)

# copied from Hui Wenteo https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('enterprises:inspectionCalendar'))
    return render(request, 'enterprises/event.html', {'form': form})