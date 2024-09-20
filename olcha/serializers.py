from rest_framework import serializers
from olcha.models import Category, Group
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        context = super(CategorySerializer, self).to_representation(instance)
        context['updated_at'] = datetime.now()
        return context


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        context = super(GroupSerializer, self).to_representation(instance)
        context['updated_at'] = datetime.now()
        return context
