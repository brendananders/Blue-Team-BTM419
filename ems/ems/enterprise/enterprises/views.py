from django.shortcuts import render, redirect
from .models import *
from .forms import ClaimForm
from django.contrib.auth.decorators import login_required
# copied from Hui Wenteo https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar



# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'enterprises/index.html')

def claims(request):
    """claims main menu"""
    return render(request, 'enterprises/claims.html')

@login_required
def claimsIndex(request):
    """claims index"""
    claimsList=Claim.objects.order_by('claimDate')
    context={'claimsIndex':claimsList}
    return render(request, 'enterprises/claimsIndex.html')
    
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
    return render(request, 'enterprises/warranties.html')

def inspections(request):
    """inspections main menu"""
    return render(request, 'enterprises/inspections.html')

@login_required
def inspectionsIndex(request):
    """inspections index"""
    inspectionsList=Inspection.objects.order_by('inspectionDate')
    context={'inspectionsIndex':inspectionsList}
    return render(request, 'enterprises/inspectionsIndex.html')

@login_required
def newInspection(request):
    """Add a new inspection."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClaimForm()
    else:
        # POST data submitted; process data.
        form = ClaimForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprises:inspectionsIndex')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'enterprises/newInspection.html', context)

# copied from Hui Wenteo https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

class CalendarView(generic.ListView):
    model = Inspection
    template_name = 'enterprises/inspectionCalendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()