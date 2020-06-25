from django.test import TestCase
from substitutes.forms import SearchForm


class TestForms(TestCase):

    def test_expense_form_valid_data(self):
        form = SearchForm(data={
            "research": "Cerise"
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
