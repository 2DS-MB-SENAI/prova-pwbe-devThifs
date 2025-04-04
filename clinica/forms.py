from .models import Consulta, Medico
from django import forms

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'