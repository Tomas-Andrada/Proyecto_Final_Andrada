from django import forms

class MensajeForm(forms.Form):
    contenido = forms.CharField(max_length=200)