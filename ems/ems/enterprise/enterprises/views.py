from django.shortcuts import render, redirect
from .models import Claim, Warranty
from .forms import ClaimForm
from django.contrib.auth.decorators import login_required



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