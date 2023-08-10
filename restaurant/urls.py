from django.urls import path

from restaurant.views import (index,
                              FoodListView,
                              DishTypeCreateView,
                              FoodDetailView,
                              CookerDetailView,
                              DishCreateView,
                              CookerCreateView,
                              FoodUpdateView, FoodDeleteView,
                              )

urlpatterns = [
    path("", index, name="index"),
    path("category/create/", DishTypeCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/", FoodListView.as_view(), name="food-list"),
    path("category/dish/<int:pk>/", FoodDetailView.as_view(), name="food-detail"),
    path("category/dish/<int:pk>/update/", FoodUpdateView.as_view(), name="food-update"),
    path("category/dish/<int:pk>/delete/", FoodDeleteView.as_view(), name="food-delete"),
    path("category/dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("accounts/signin/", CookerCreateView.as_view(), name="account-create"),
    path("accounts/<int:pk>/", CookerDetailView.as_view(), name="account-detail"),
]

app_name = "restaurant"
