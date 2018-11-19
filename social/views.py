from django.shortcuts import render
from .models import Link

def links(request):
    links = Link.objects.all()
    return render(request, 'social/links.html', {'links':links})