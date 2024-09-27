from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from olcha.serializers import ProductSerializer
from olcha.models import Product


class ProductCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


