from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.username}, ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(
        Cook
    )

    def __str__(self):
        return f"{self.name}"
