from django import forms
from home.models import Objective

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['description', 'completed']
        widgets = {
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
