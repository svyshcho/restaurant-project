from django.contrib import admin
from django.urls import path

from restaurant.views import index, FoodListView, DishTypeCreateView, FoodDetailView

urlpatterns = [
    path("", index, name="index"),
    path("category/create/", DishTypeCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/", FoodListView.as_view(), name="food-list"),
    path("category/<int:pk>/<int:dish_pk>", FoodDetailView.as_view(), name="food-detail"),
]

app_name = "restaurant"
