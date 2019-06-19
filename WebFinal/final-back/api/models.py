from django.db import models
from django.contrib.auth.models import User


class ProductManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }


class UserProduct(models.Model):
    user = models.CharField(max_length=200)
    count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.user)

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user,
            'count': self.count,
        }


