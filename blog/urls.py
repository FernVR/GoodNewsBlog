from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('profile', views.user_profile, name='user_profile'),
    path('profile/update/', views.profile_update_view, name='profile-update'),
    path('profile/delete/', views.profile_delete_view, name='profile-delete'),

]