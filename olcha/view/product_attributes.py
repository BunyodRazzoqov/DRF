from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from olcha.models import ProductAttribute, AttributeKey, AttributeValue
from olcha.serializers import ProductAttributeSerializer, AttributeKeySerializer, AttributeValueSerializer


class ProductAttributesApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductAttributeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    lookup_field = 'pk'


class AttributeKeyApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer


class AttributeKeyDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer
    lookup_field = 'pk'


class AttributeValueApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class AttributeValueDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
    lookup_field = 'pk'
