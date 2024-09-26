from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Count 
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile, Like
from .forms import CommentForm, UserPostForm
import bleach

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).annotate(comment_count=Count('comments')).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 2


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()
    user_post_form = UserPostForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_post_form": user_post_form,
            },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    # Toggle like/dislike
    if created:  # If a new like is created
        like.like_type = True  # This means the user liked the post
        like.save()
    else:  # If the user already liked/disliked the post
        like.delete()  # Remove the like/dislike
        return redirect('post_detail', post_id=post.id)

    return redirect('post_detail', post_id=post.id)

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    # Toggle dislike
    if created:  # If a new dislike is created
        like.like_type = False  # This means the user disliked the post
        like.save()
    else:  # If the user already liked/disliked the post
        like.delete()  # Remove the like/dislike
        return redirect('post_detail', post_id=post.id)

    return redirect('post_detail', post_id=post.id)


def user_profile(request):
    """
    View for displaying the user profile and handling new post submissions.
    """
    # Get the logged-in user's profile
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        user_post_form = UserPostForm(data=request.POST)
        if user_post_form.is_valid():
            post = user_post_form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your post has been submitted and is awaiting approval.'
            )
            return redirect('user_profile')  # Redirect to the user profile page after saving

    else:
        user_post_form = UserPostForm()  # Initialize an empty form for GET requests

    return render(
        request,
        "blog/user_profile.html",
        {
            'profile': profile,
            'user_post_form': user_post_form,  # Pass the form to the template
        },
    )


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)



@login_required
def profile_update_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('home')  # Redirect to home after deletion

    return render(request, 'profile_delete.html')