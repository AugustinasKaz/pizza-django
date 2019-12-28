# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Salad, Order, Pasta, Regular_Pizza, Topping, Sicilian_Pizza, Dinner_Platters, Subs

admin.site.register(Salad)
admin.site.register(Pasta)
admin.site.register(Order)
admin.site.register(Topping)
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Dinner_Platters)
admin.site.register(Subs)
