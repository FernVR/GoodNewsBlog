from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Post, Comment, Profile
from .forms import CommentForm, UserPostForm


class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post.objects.create(
            title="Blog title",
            author=self.user,
            slug="blog-title",
            excerpt="Blog excerpt",
            content="Blog content",
            status=1
        )

    
    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blog title")
        self.assertContains(response, "Blog content")
        self.assertIsInstance(response.context['comment_form'], CommentForm)