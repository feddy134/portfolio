from django.shortcuts import render
from .models import Jobs

# Create your views here.
def home(request):
    job = Jobs.objects
    return render(request,'jobs/home.html',{'job': job})
