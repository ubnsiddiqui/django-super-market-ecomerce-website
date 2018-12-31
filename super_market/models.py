from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150)
    detail = models.TextField(max_length=500)
    price = models.FloatField(null=False, blank=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', default='media/blank.jpg')


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.FloatField()


# class Order(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100)
#
#
# class OrderDetail(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#


