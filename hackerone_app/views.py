from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import HackerOneProgram, Engineer

def dashboard(request):
    programs = HackerOneProgram.objects.all()
    engineers = Engineer.objects.order_by('-rank')
    # Fetch HackerOne programs periodically using the API (we'll cover this in Step 9)
    return render(request, 'hackerone_app/dashboard.html', {'programs': programs, 'engineers': engineers})
