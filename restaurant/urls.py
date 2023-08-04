from django.contrib import admin
from django.urls import path

from restaurant.views import index, FoodListView

urlpatterns = [
    path("", index, name="index"),
    path("category/<int:pk>", FoodListView.as_view(), name="food-list"),
]

app_name = "restaurant"
