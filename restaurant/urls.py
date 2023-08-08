from django.contrib import admin
from django.urls import path

from restaurant.views import index, FoodListView, DishTypeCreateView, FoodDetailView, DishCreateView

urlpatterns = [
    path("", index, name="index"),
    path("category/create/", DishTypeCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/", FoodListView.as_view(), name="food-list"),
    path("category/dish/<int:pk>/", FoodDetailView.as_view(), name="food-detail"),
    path("category/dish/create/", DishCreateView.as_view(), name="dish-create"),
]

app_name = "restaurant"
