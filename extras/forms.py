from django import forms
from models import ImagenAdjunta

class AdjuntaForm(forms.ModelForm):
    class Meta:
        model = ImagenAdjunta


