from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(form.is_valid(), msg='Form should be valid with non-empty body')

    def test_form_is_invalid(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid(), msg="Form should be invalid with empty body")
