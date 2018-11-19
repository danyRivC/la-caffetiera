from django.shortcuts import render
from services.models import Services
# Create your views here.
def services(request):
    service = Services.objects.all()
    return render(request, 'services/services.html', {'services':service})