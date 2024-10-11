from django.core.cache import cache
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import viewsets
from post.models import Post
from post.permissions import MyIsAuthenticate, IsAdminPermission
from post.serializers import PostSerializer


# Create your views here.


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cache_key = 'post_list'
        cached_data = cache.get(cache_key)
        if not cached_data:
            queryset = Post.objects.all().select_related('user')
            queryset = queryset.prefetch_related('user__groups')
            queryset = queryset.prefetch_related('user__user_permissions')
            cache.set(cache_key, queryset, timeout=60 * 1)
            return queryset
        return cached_data


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminPermission]
    lookup_field = 'pk'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
