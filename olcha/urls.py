from django.urls import path
from olcha.view import category, group, product

urlpatterns = [
    path('categories/', category.CategoryList.as_view(), name='categories'),
    path('groups/', group.GroupList.as_view(), name='groups'),
    path('categories/detail/<int:pk>/', category.CategoryDetailApiView.as_view(), name='categories_detail'),
    path('groups/detail/<int:pk>/', group.GroupDetailApiView.as_view(), name='groups_detail'),
    path('products/', product.ProductCreate.as_view(), name='products'),
    path('products/detail/<slug:slug>/', product.ProductDetail.as_view(), name='products_detail'),
]
