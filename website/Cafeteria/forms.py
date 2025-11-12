
from django import forms
from .models import reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = reseña
        fields = ['nombre_cliente', 'calificacion', 'comentario']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Nombre'}),
            'calificacion': forms.Select(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu experiencia'}),
        }
