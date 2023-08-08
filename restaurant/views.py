from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from restaurant.forms import DishTypeCreationForm, DishCreationForm
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


class FoodListView(generic.ListView):
    model = Dish
    context_object_name = "dishes_list"
    template_name = "restaurant/dishes_list.html"

    def get_queryset(self):
        dish_type = self.kwargs["pk"]
        queryset = Dish.objects.filter(dish_type__id=dish_type)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_pk = self.kwargs["pk"]
        dish_type = get_object_or_404(DishType, pk=dish_pk)
        context["dish_type"] = dish_type
        context["dish_type_list"] = DishType.objects.all()
        return context


class FoodDetailView(generic.DetailView):
    template_name = "restaurant/dish_detail.html"
    context_object_name = "dish"
    model = Dish

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish_type_list"] = DishType.objects.all()
        return context


class DishTypeCreateView(generic.CreateView):
    form_class = DishTypeCreationForm
    success_url = reverse_lazy("catalog:index")
    template_name = "restaurant/catalog_create.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish_type_list"] = DishType.objects.all()
        return context


class DishCreateView(generic.CreateView):
    form_class = DishCreationForm
    success_url = reverse_lazy("catalog:index")
    template_name = "restaurant/dish_create.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish_type_list"] = DishType.objects.all()
        return context
