from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('login/', views.user_login, name='user_login'),  # URL for user login
    path('logout/', views.user_logout, name='user_logout'),  # URL for user logout
    path('posts/', views.post_list, name='post_list'),
    path('edit_post/', views.edit_post, name='edit_post'),
]
