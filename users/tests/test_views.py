"""
For more informations about django test :
https://docs.djangoproject.com/en/2.2/topics/testing/overview/

"""
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="testing"
        )

    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.get(reverse("register"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    @login_required
    def test_profile_connected(self):
        self.client.login(username="test", password="testing")
        response = self.client.get(reverse("profile"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    @login_required
    def test_profile_no_connected(self):
        response = self.client.get(reverse("profile"))
        self.assertEquals(response.status_code, 302)

    def test_login(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    @login_required
    def test_logout_connected(self):
        self.client.login(username="test", password="testing")
        response = self.client.get(reverse("logout"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')
