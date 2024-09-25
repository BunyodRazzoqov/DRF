from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Group(BaseModel):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='groups')
    image = models.ImageField(upload_to='group/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Groups'


class Product(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    discount = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    users_like = models.ManyToManyField(User, related_name='products', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='products')

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)

        return self.price

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'products'


class Image(BaseModel):
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = 'image'

    @property
    def is_primary_image(self):
        if self.is_primary:
            return self.image

    def __str__(self):
        return str(self.id)


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='orders')
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    first_payment = models.FloatField(null=True, blank=True, default=0)
    month = models.PositiveSmallIntegerField(default=3, null=True, blank=True,
                                             validators=[MinValueValidator(3), MaxValueValidator(12)])

    @property
    def monthly_payment(self):
        return self.product.price // self.month

    def __str__(self):
        return f'{self.product.name} - {self.user.username} - {self.quantity}'


class Comment(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    message = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='comments/%Y/%m/%d/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO.value,
                                              null=True)

    def __str__(self):
        return self.message


class Attribute(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'attribute'


class AttributeValue(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        db_table = 'attribute_value'


class ProductAttribute(BaseModel):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
