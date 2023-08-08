from django import forms
from restaurant.models import DishType, Dish, Cook
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class DishTypeCreationForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishCreationForm(forms.ModelForm):
    dish_type = forms.ModelChoiceField(
        queryset=DishType.objects.all(),
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self):
        return validate_license_number(self.cleaned_data["years_of_experience"])


def validate_license_number(years):
    if years < 0:
        raise ValidationError("Min years value is 0")
    return years
