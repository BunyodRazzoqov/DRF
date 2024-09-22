from django.contrib import admin

from olcha.models import Category, Group, Product


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    search_fields = ('id', 'title', 'slug')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    search_fields = ('id', 'title', 'slug')
    list_filter = ('created_at',)
    prepopulated_fields = ({'slug': ('title',)})


@admin.register(Product)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'price')
    search_fields = ('id', 'name', 'slug', 'price')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
