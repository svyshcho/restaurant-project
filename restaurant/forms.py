from django import forms
from restaurant.models import DishType, Dish, Cook
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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


# class CookerCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta):
#         model = Cook
