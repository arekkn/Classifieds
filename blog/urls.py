from django.urls import path
from . import views
from .views import PostListView, PostUpdateView, PostCreateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('posts/<int:pk>', views.post, name='post'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
