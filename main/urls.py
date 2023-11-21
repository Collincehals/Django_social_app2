from django.urls import path
from . import views

urlpatterns = [
    path('', views.Posts, name='posts'),
    path('category/<tag>/', views.Posts, name='category'),
    path('create/post/', views.create_post, name='create_post'),
    path('post/<pk>/', views.PostPage, name='post'),
    path('post/delete/<pk>/', views.PostDelete, name='post-delete'),
    path('post/edit/<pk>/', views.PostEditView, name='post-edit'),
    path('profile/', views.Profile, name='profile'),
    path('<username>/', views.Profile, name='user-profile'),
    path('profile/edit/', views.EditProfileView, name='profile-edit'),
    path('profile/delete/', views.DeleteProfile, name='profile-delete'),
    path('url/videos', views.URLVideos, name='url-videos'),
]

