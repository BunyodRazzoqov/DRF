from django.urls import path
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet

from post.views import PostListView, PostDetailApiView


router = DefaultRouter()
router.register(r'my_post_list', PostViewSet, basename='post')

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailApiView.as_view(), name='post_detail')
]
urlpatterns += router.urls