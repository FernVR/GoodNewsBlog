from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Count, Q
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile
from .forms import CommentForm, UserPostForm, ProfileUpdateForm
import bleach

# Create your views here.

class PostList(generic.ListView):
    """
    View to display paginated list of posts on home page.
    """
    queryset = Post.objects.filter(
        status=1).annotate(
            comment_count=Count(
                'comments', filter=Q(
                    comments__approved=True))).order_by("-created_on")
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


@login_required
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
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
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
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def user_profile(request):
    """
    View for displaying the user profile and handling new post submissions.
    """
    # Get the logged-in user's profile
    profile = get_object_or_404(Profile, user=request.user)
    # Get the posts created by the logged-in user
    user_posts = Post.objects.filter(author=request.user)

    if request.method == "POST":
        user_post_form = UserPostForm(data=request.POST, files=request.FILES)
        if user_post_form.is_valid():
            post = user_post_form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your post has been submitted and is awaiting approval.'
            )
            return redirect('user_profile')  # Redirect to the user profile

    else:
        user_post_form = UserPostForm()

    return render(
        request,
        "blog/user_profile.html",
        {
            'profile': profile,
            'user_post_form': user_post_form,  # Pass the form to the template
            'user_posts': user_posts,  # Pass the user's posts to the template
        },
    )


def custom_404_view(request, exception):
    """
    View to render 404 page.
    """
    return render(request, '404.html', status=404)


@login_required
def profile_update_view(request):
    """
    View to update profile information. 
    """
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user_profile')

    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'blog/profile_update.html', {
        'profile_form': profile_form
    })


@login_required
def profile_delete_view(request):
    """
    View to delete profile. 
    """
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('home')  # Redirect to home after deletion

    return render(request, 'blog/profile_delete.html')


@login_required
def post_delete(request, slug):
    """
    View to delete user posts from post list. 
    """
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Your post has been deleted.")
        return redirect('user_profile')  # Redirect to the user's profile


