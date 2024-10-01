from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

STATUS = ((0, "Unapproved"), (1, "Approved"))

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder', blank=True, null=True)  # Set blank=True and null=True for optional image
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.CharField(max_length=500, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Generate a slug from the title if it doesn't exist
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"



class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: ' {self.body} ' by {self.author}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_type = models.BooleanField(default=True)  # True for like, False for dislike

    class Meta:
        unique_together = (
            'user', 'post')  # Prevent multiple likes/dislikes from the same user



class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_img = CloudinaryField('image', default='placeholder') 
    bio = models.TextField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.user.username


# Signal to create a profile when a new user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()