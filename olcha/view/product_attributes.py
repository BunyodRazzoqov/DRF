from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from olcha.models import ProductAttribute, AttributeKey, AttributeValue
from olcha.serializers import ProductAttributeSerializer, AttributeKeySerializer, AttributeValueSerializer


class ProductAttributesApi(ListCreateAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductAttributeDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    lookup_field = 'pk'


class AttributeKeyApiView(ListCreateAPIView):
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer


class AttributeKeyDetail(RetrieveUpdateDestroyAPIView):
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer
    lookup_field = 'pk'


class AttributeValueApiView(ListCreateAPIView):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class AttributeValueDetail(RetrieveUpdateDestroyAPIView):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
    lookup_field = 'pk'
