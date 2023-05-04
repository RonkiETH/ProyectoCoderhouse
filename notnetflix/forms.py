from django import forms

class PeliculaForm(forms.Form):
    titulo = forms.CharField()
    orden = forms.IntegerField()
    descripcion = forms.CharField()

class SerieForm(forms.Form):
    titulo = forms.CharField()
    orden = forms.IntegerField()
    descripcion = forms.CharField()

class AnimeForm(forms.Form):
    titulo = forms.CharField()
    orden = forms.IntegerField()
    descripcion = forms.CharField()