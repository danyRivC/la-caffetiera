from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Escribe tu Nombre'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':'Escribe tu Email'}))
    content = forms.CharField(label='Mensaje', required=True,  widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder':'Deja un comentario'}))