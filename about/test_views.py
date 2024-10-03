from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


class TestAboutViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.about = About.objects.create(
            title="About Title",
            content="About Content",
            updated_on="2024-01-01"
        )

    def test_about_me_view_get(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Title")
        self.assertContains(response, "About Content")
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    