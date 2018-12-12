from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import contactForm
from django.urls import reverse
# Create your views here.
def contact(request):
    form_contact = contactForm

    if request.method=='POST':
        form_contact = contactForm(data=request.POST)
        if form_contact.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                "La cafetiera: nuevo correo de Contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["django-155605@inbox.mailtrap.io"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?ok")

    return render(request, 'contact/contact.html', {'contact': form_contact})