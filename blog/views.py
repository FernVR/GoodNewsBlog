from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Count 
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile
from .forms import CommentForm, UserPostForm

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
    
    if request.method == "POST":
        user_post_form = UserPostForm(data=request.POST)
        if user_post_form.is_valid():
            post = user_post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your post has been submitted and awaiting approval'
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


def user_profile(request):
    """
    """
    pk = request.user
    profile = Profile.objects.all()
    obj = get_object_or_404(profile, pk=1)

    if request.method == "POST":
        user_post_form = UserPostForm(data=request.POST)
        if user_post_form.is_valid():
            post = user_post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your post has been submitted and awaiting approval'
            )

    user_post_form = UserPostForm()
    
    return render(
        request,
        "blog/user_profile.html",
        {
            'profile': profile
            },
    )


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)