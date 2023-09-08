from django import forms

class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField()
    imagen = forms.FileField()
    