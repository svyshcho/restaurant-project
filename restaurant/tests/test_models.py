from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish


class ModelTests(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cooker = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="test",
            last_name="test"
        )

        self.assertEqual(str(cooker), f"{cooker.username}, ({cooker.first_name} {cooker.last_name})")

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        dish = Dish.objects.create(
            name="test",
            description="test",
            price=11,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), dish.name)
