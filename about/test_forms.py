from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """
    Test Feedback/Collaboration form.
    """
    def test_form_is_valid(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'I would love to collaborate with you.'
        }
        form = CollaborateForm(form_data)
        self.assertTrue(
            form.is_valid(), msg='Form should be valid with all fields filled')

    def test_form_is_invalid_missing_fields(self):
        form_data = {
            'name': '',  # Missing name should make the form invalid
            'email': 'john@example.com',
            'message': 'I would love to collaborate with you.'
        }
        form = CollaborateForm(form_data)
        self.assertFalse(
            form.is_valid(), msg="Form should be invalid with missing name")

    def test_form_is_invalid_email_format(self):
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email',  # Invalid email format
            'message': 'I would love to collaborate with you.'
        }
        form = CollaborateForm(form_data)
        self.assertFalse(
            form.is_valid(),
            msg="Form should be invalid with incorrect email format")
