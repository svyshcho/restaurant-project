from django import forms

from restaurant.models import DishType


class DishTypeCreationForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]
