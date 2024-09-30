from .models import Comment, Post, Profile
from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            
            'class': 'form-control',  # Bootstrap styling
            'style': 'border-radius: 2em', # Border radius
            'style': 'height: 120px;',  # Adjust the height
            
        })


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content',)
        widgets = {
            'content': SummernoteWidget(),  # Use Summernote widget for your content field
        }
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_img',]