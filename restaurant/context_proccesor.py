from .models import DishType


def dish_type_list(request):
    return {
        "dish_type_list": DishType.objects.all()
    }
