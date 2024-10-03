from django.test import TestCase
from .forms import CommentForm, UserPostForm, ProfileUpdateForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(form.is_valid(), msg='Form should be valid with non-empty body')

    def test_form_is_invalid(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid(), msg="Form should be invalid with empty body")


class TestUserPostForm(TestCase):

    def test_form_is_valid(self):
        form_data = {
            'title': 'Sample Post',
            'excerpt': 'This is a sample excerpt',
            'content': 'This is the content of the post',
            # You might need to adjust or mock the featured_image depending on your test environment
        }
        form = UserPostForm(form_data)
        self.assertTrue(form.is_valid(), msg='Form should be valid with all fields filled')

    def test_form_is_invalid(self):
        form_data = {
            'title': '',  # Missing title should make the form invalid
            'excerpt': 'This is a sample excerpt',
            'content': 'This is the content of the post',
        }
        form = UserPostForm(form_data)
        self.assertFalse(form.is_valid(), msg="Form should be invalid with missing title")

class TestProfileUpdateForm(TestCase):

    def test_form_is_valid(self):
        form_data = {
            'bio': 'This is a sample bio',
            'location': 'Sample Location',
            # You might need to mock the profile_img in actual test cases
        }
        form = ProfileUpdateForm(form_data)
        self.assertTrue(form.is_valid(), msg='Form should be valid with all fields filled')

    def test_form_is_invalid(self):
        form_data = {
            'bio': '',  # Empty bio should be valid if not required
            'location': '',  # Empty location should be valid if not required
        }
        form = ProfileUpdateForm(form_data)
        self.assertTrue(form.is_valid(), msg='Form should still be valid with optional fields left empty')

