from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Mensaje')