from rest_framework import serializers
from olcha.models import Category, Group, Product
from datetime import datetime


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        context = super(GroupSerializer, self).to_representation(instance)
        context['updated_at'] = datetime.now()
        return context


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'full_image_url', 'created_at', 'updated_at', 'groups_count', 'groups']

    groups = GroupSerializer(many=True, read_only=True)
    full_image_url = serializers.SerializerMethodField()
    groups_count = serializers.SerializerMethodField(method_name='count')

    def count(self, obj):
        count = obj.groups.count()
        return count

    def get_full_image_url(self, instance):

        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    def to_representation(self, instance):
        context = super(CategorySerializer, self).to_representation(instance)
        context['updated_at'] = datetime.now()
        return context


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        context = super(ProductSerializer, self).to_representation(instance)
        context['updated_at'] = datetime.now()
        return context
