from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish, DishType


class PublicDishTests(TestCase):

    def setUp(self):
        self.dish_type = DishType.objects.create(name='Main Course')
        self.dish = Dish.objects.create(
            name='Test Dish', description='A test dish', price=10, dish_type=self.dish_type
        )

    def test_login_required_dish_update(self):
        dish_update_url = reverse("restaurant:food-update", kwargs={'pk': self.dish.pk})
        res = self.client.get(dish_update_url)

        self.assertNotEquals(res.status_code, 200)

    def test_login_required_dish_create(self):
        dish_create_url = reverse("restaurant:dish-create")
        res = self.client.get(dish_create_url)

        self.assertNotEquals(res.status_code, 200)

    def test_login_required_dish_type_create(self):
        dish_type_create = reverse("restaurant:category-create")
        res = self.client.get(dish_type_create)

        self.assertNotEquals(res.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="admin12345"
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name='Main Course')
        self.dish = Dish.objects.create(
            name='Test Dish', description='A test dish', price=10, dish_type=self.dish_type
        )

    def test_create_dish_when_login(self):
        dish_create_url = reverse("restaurant:dish-create")
        res = self.client.get(dish_create_url)

        self.assertEquals(res.status_code, 200)

    def test_update_dish_when_login(self):
        dish_update_url = reverse("restaurant:food-update", kwargs={'pk': self.dish.pk})
        res = self.client.get(dish_update_url)

        self.assertEquals(res.status_code, 200)

    def test_create_dish_type_when_login(self):
        dish_type_create = reverse("restaurant:category-create")
        res = self.client.get(dish_type_create)

        self.assertEquals(res.status_code, 200)
