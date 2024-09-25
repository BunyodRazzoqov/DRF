from django.db.models import Avg
from rest_framework import serializers
from olcha.models import Category, Group, Product, Comment
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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    all_images = serializers.SerializerMethodField()
    users_comment = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    count_comments = serializers.SerializerMethodField(method_name='counts')
    users_like = serializers.BooleanField()
    ratings = serializers.SerializerMethodField()

    def get_ratings(self, obj):
        ratings = obj.comments.all().values_list('rating', flat=True).aggregate(avg=Avg('rating'))
        return ratings

    def get_users_like(self, obj):
        if obj.users_like:
            obj.users_like = True
        else:
            obj.users_like = False

        return obj.users_like

    def counts(self, obj):
        count = obj.comments.count()
        return count

    def get_all_images(self, obj):
        request = self.context.get('request')
        images = [request.build_absolute_uri(image.image.url) for image in obj.images.all()]
        return images

    def get_users_comment(self, obj):
        comments = [comment.user.username for comment in obj.comments.all()]
        return comments

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        context = super(ProductSerializer, self).to_representation(instance)
        context['updated_at'] = datetime.now()
        return context
