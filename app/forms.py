# core/forms.py
from django import forms

class AccionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    accion = forms.ChoiceField(choices=[('analizar', 'Analizar'),
                                        ('generar', 'Generar')])
