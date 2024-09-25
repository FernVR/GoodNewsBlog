from .models import Comment, Post, Profile
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content',)
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_img',]