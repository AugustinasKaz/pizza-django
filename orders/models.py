from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format({self.name})


class Regular_Pizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    large = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return "{} - {} - {}".format({self.name}, {self.small}, {self.large})


class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    large = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return "{} - {} - {}".format({self.name}, {self.small}, {self.large})


class Dinner_Platters(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    large = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return "{} - {} - {}".format({self.name}, {self.small}, {self.large})


class Subs(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    large = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return "{} - {} - {}".format({self.name}, {self.small}, {self.large})


class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(null=True)

    def __str__(self):
        return "{} - {}".format({self.name}, {self.price})


class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(null=True)

    def __str__(self):
        return "{} - {}".format({self.name}, {self.price})


class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    topping_allowed = models.BooleanField(default=False)
    topping_number_allowed = models.BooleanField(default=True)
    topping_number = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topps = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return "{} # {} # {} # {}".format({self.name}, {self.topps.all()}, {self.topping_number_allowed}, {self.topping_allowed})
