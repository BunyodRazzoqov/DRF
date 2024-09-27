from django.urls import path
from olcha.view import category, group, product, product_attributes

urlpatterns = [
    path('categories/', category.CategoryList.as_view()),
    path('groups/', group.GroupList.as_view()),
    path('categories/detail/<int:pk>/', category.CategoryDetailApiView.as_view()),
    path('groups/detail/<int:pk>/', group.GroupDetailApiView.as_view()),
    path('products/', product.ProductCreate.as_view()),
    path('products/detail/<slug:slug>/', product.ProductDetail.as_view()),

    path('product/productattributes/', product_attributes.ProductAttributesApi.as_view()),
    path('product/productattributes/detail/<int:pk>/', product_attributes.ProductAttributeDetail.as_view()),

    path('product/attributekeys/', product_attributes.AttributeKeyApiView.as_view()),
    path('product/attributekeys/detail/<int:pk>/', product_attributes.AttributeKeyDetail.as_view()),

    path('product/attributevalues/', product_attributes.AttributeValueApiView.as_view()),
    path('product/attributevalues/detail/<int:pk>/', product_attributes.AttributeValueDetail.as_view()),
]
