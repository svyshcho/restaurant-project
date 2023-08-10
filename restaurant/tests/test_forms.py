from django.test import TestCase

from restaurant.forms import CookerCreationForm


class FormTests(TestCase):
    def test_cooker_creation_form_with_year_of_experience(self):
        form_data = {
            "username": "new_user",
            "password1": "ssendam31",
            "password2": "ssendam31",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 1,
        }

        form = CookerCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_json())
        self.assertEqual(form.cleaned_data, form_data)
