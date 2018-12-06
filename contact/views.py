from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def contact(request):
    form_contact=contactForm
    return render(request, 'contact/contact.html', {'contact': form_contact})