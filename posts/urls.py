from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.createPost, name='Create Post'),
    path('lost_post_overall/', views.postOverall, name='Lost Post Overall'),
    path('lost_post_detail/<int:post_id>/', views.postDetail, name='Lost Post Detail'),  
    path('user_posts/', views.userPosts, name='User Posts'),
    path('lost_post_detail/<int:post_id>/delete', views.delete_post, name='Delete Post'),
    path('lost_post_detail/<int:post_id>/edit', views.edit_post, name='Edit Post'),  
]