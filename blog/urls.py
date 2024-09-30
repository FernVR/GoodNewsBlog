from . import views
from django.urls import path
from .views import like_post, dislike_post

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/update/', views.profile_update_view, name='profile-update'),
    path('profile/delete/', views.profile_delete_view, name='profile-delete'),
    
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('post/<slug:slug>/like/', like_post, name='like_post'),
    path('post/<slug:slug>/dislike/', dislike_post, name='dislike_post'),
]