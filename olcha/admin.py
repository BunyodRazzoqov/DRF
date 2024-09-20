from django.contrib import admin

from olcha.models import Category, Group


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    search_fields = ('id', 'title', 'slug')
    list_filter = ('created_at',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    search_fields = ('id', 'title', 'slug')
    list_filter = ('created_at',)
