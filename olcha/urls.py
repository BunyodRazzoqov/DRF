from django.urls import path
from olcha.views import CategoryDetailApiView, CategoryList, GroupList, GroupDetailApiView, ProductCreate, ProductDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('groups/', GroupList.as_view(), name='groups'),
    path('categories/detail/<int:pk>/', CategoryDetailApiView.as_view(), name='categories_detail'),
    path('groups/detail/<int:pk>/', GroupDetailApiView.as_view(), name='groups_detail'),
    path('products/', ProductCreate.as_view(), name='products'),
    path('products/detail/<slug:slug>/', ProductDetail.as_view(), name='products_detail'),
]
