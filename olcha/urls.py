from django.urls import path
from olcha.views import CategoryDetailApiView, CategoryList, GroupList, GroupDetailApiView

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('groups/', GroupList.as_view(), name='groups'),
    path('categories/detail/<int:pk>/', CategoryDetailApiView.as_view(), name='categories_detail'),
    path('groups/detail/<int:pk>/', GroupDetailApiView.as_view(), name='groups_detail'),
]
