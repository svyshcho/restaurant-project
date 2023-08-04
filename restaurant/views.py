from django.shortcuts import render

from restaurant.models import DishType, Dish, Cook


def index(request):
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_cookers = Cook.objects.count()
    dish_type_list = DishType.objects.all()

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cookers": num_cookers,
        "dish_type_list": dish_type_list

    }

    return render(request, "restaurant/index.html", context=context)

