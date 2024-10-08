from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Post, Comment, Profile
from .forms import CommentForm, UserPostForm


class TestBlogViews(TestCase):
    """
    View to test blog views.
    """
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

    def test_successful_comment_submission(self):
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Comment submitted and awaiting approval')
    
    def test_comment_edit(self):
        comment = Comment.objects.create(
            post=self.post, author=self.user, body='Original Comment'
        )
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(
            reverse('comment_edit', args=['blog-title', comment.id]), {
                'body': 'Updated Comment'
            })
        self.assertRedirects(
            response, reverse('post_detail', args=['blog-title']))
        comment.refresh_from_db()
        self.assertEqual(comment.body, 'Updated Comment')

    def test_comment_delete(self):
        comment = Comment.objects.create(
            post=self.post, author=self.user, body='Comment to be deleted'
        )
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(
            reverse('comment_delete', args=['blog-title', comment.id]))
        self.assertRedirects(
            response, reverse('post_detail', args=['blog-title']))
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_user_profile_view(self):
        self.client.login(username="myUsername", password="myPassword")

        # Simulate submitting a post via POST request
        post_data = {
            'title': 'Test Post',
            'excerpt': 'Test excerpt',
            'content': 'This is the content of the test post.',
            'featured_image': '',  # Optional field, can leave empty
        }

        response = self.client.post(reverse('user_profile'), post_data)

        # Check if the response contains the success message after submission
        # Expecting a redirect after successful post submission
        self.assertEqual(response.status_code, 302)

        # Follow the redirect and check if the success message is present
        follow_response = self.client.get(reverse('user_profile'))
        self.assertContains(
            follow_response,
            'Your post has been submitted and is awaiting approval.')

    def test_profile_update_view(self):
        self.client.login(username="myUsername", password="myPassword")

        # Fetch the existing profile for the user
        profile = Profile.objects.get(user=self.user)

        # Set initial values for the profile
        profile.bio = 'Initial Bio'  # Ensure there's an initial value
        profile.location = 'Initial Location'
        profile.save()  # Save the initial state

        response = self.client.post(reverse('profile-update'), {
            'bio': 'Updated Bio',
            'location': 'Updated Location'
        })

        self.assertRedirects(response, reverse('user_profile'))

        # Refresh the profile instance to get updated values
        profile.refresh_from_db()

        self.assertEqual(profile.bio, 'Updated Bio')
        # Check the updated location too
        self.assertEqual(profile.location, 'Updated Location')

    def test_post_delete_view(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(
            reverse('post_delete', args=['blog-title']))
        self.assertRedirects(response, reverse('user_profile'))
        self.assertFalse(Post.objects.filter(slug='blog-title').exists())
        