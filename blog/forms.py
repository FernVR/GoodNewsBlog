from .models import Comment, Post, Profile
from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Comment form.
    adds styling so comment box appears smaller on the page. 
    """
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({

            'class': 'form-control',  # Bootstrap styling
            'style': 'border-radius: 2em',  # Border radius
            'style': 'height: 120px;',  # Adjust the height

        })


class UserPostForm(forms.ModelForm):
    """
    User post form
    Uses summernote text editor as content field.
    """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content', 'featured_image')
        widgets = {
            # Use Summernote widget for your content field
            'content': SummernoteWidget(),
        }


class ProfileUpdateForm(forms.ModelForm):
    """
    Form to update profile information. 
    """
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_img', ]
