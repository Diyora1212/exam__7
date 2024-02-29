from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, URLField, ForeignKey, CASCADE, EmailField, Model, DateTimeField, \
    IntegerField


class AbstractModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = ImageField(upload_to="users/avatar/%Y/%m/%d", default="user_avatar.jpg")

    class Meta:
        # Add any other Meta options
        swappable = 'AUTH_USER_MODEL'


User._meta.get_field('groups').related_query_name = 'product_user_groups'
User._meta.get_field('user_permissions').related_query_name = 'product_user_permissions'


class ProductAuthor(AbstractModel):
    first_name = CharField(max_length=56)
    last_name = CharField(max_length=56)
    website = URLField()
    avatar = ImageField(upload_to="authors/avatar/%Y/%m/%d")
    like_count = IntegerField(default=0)

    def total_likes(self):
        return self.total_likes()


class Product(AbstractModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d')
    description = models.TextField(default=None)
    owner = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    authors = ForeignKey(ProductAuthor, on_delete=CASCADE, related_name='products')

    def __str__(self):
        return self.name
