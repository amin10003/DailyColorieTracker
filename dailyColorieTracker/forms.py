from django import forms
from .models import *

class FoodForm(forms.ModelForm):
    """
    
    Form for creating a new food
    """
    
    class Meta:
        model = Food
        fields = [
            "name",
            "calories"
        ]
        
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter food name",
                    "min": 0,
                }
            ),
        }
    