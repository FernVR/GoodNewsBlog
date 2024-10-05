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
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_about_me_view_post_valid_form(self):
        response = self.client.post(reverse('about'), {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'This is a collaboration request.'
        })

        # Check for a redirect response
        self.assertRedirects(response, reverse('about'))

        # Verify the success message was created
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertTrue(len(messages_list) > 0)
        self.assertEqual(str(messages_list[0]), 
                         "Your feedback has been sent. Thank you!")
