from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Salad, Order, Pasta, Regular_Pizza, Topping, Sicilian_Pizza
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'orders/home.html')


def menu(request):
    context = {
        "salads": Salad.objects.all(),
        "pastas": Pasta.objects.all(),
        "pizza1": Regular_Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "pizza2": Sicilian_Pizza.objects.all()
    }
    return render(request, 'orders/menu.html', context)

def home_menu(request):
    context = {
        "salads": Salad.objects.all(),
        "pastas": Pasta.objects.all(),
        "pizza1": Regular_Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "pizza2": Sicilian_Pizza.objects.all()
    }
    return render(request, 'orders/home_menu.html', context)

def add1(request, food_name, food_price):
    current = request.user
    ord = Order()
    if food_name == "2 toppings" or food_name == "1 topping" or food_name == "3 toppings":
        messages.success(request, f'Added {food_name} to your cart')
        ord.topping_number_allowed = True
        ord.topping_allowed = True
        ord.author = current
        ord.name = food_name
        ord.price = food_price
        ord.save()
        print(ord)
    else:
        messages.success(request, f'Added {food_name} to your cart')
        ord.author = current
        ord.name = food_name
        ord.price = food_price
        ord.save()
    return redirect("menu")


def add2(request, top_name):
    tp = Topping.objects.get(name=top_name)
    try:
        ord = Order.objects.filter(topping_allowed=True).reverse()[0]
        if ord.topping_number_allowed == True:
            if ord.name == "3 toppings":
                ord.topping_number += 3
                ord.topping_number_allowed = False
                ord.save()
            if ord.name == "2 toppings":
                ord.topping_number += 2
                ord.topping_number_allowed = False
                ord.save()
            if ord.name == "1 topping":
                ord.topping_number = 1
                ord.topping_number_allowed = False
                ord.save()
        if ord.topping_number > 0:
            ord.topping_number = ord.topping_number - 1
            ord.topps.add(tp.id)
            messages.success(request, f"added {top_name}")
            ord.save()
        if ord.topping_number <= 0:
            ord.topping_allowed = False
            ord.topping_number_allowed = True
            ord.save()
    except IndexError:
        messages.info(request, "cant add more")
    return redirect("menu")


def cart(request):
    context = {
        "orders": Order.objects.filter(author=request.user),
        "total": Order.objects.filter(author=request.user).aggregate(Sum('price')).values()
    }
    return render(request, "orders/cart.html", context)


def remove(request, food_id, food_name):
    Order.objects.filter(id=food_id).delete()
    messages.info(request, f"removed {food_name} from cart")
    return redirect("cart")


def confirm(request):
    current = request.user
    subject = 'Your Django Pizza order were confirmed'
    message = 'Your order will be delivered as soon as possible. With best regards, Django Pizza team'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [current.email, ]
    send_mail(subject, message, email_from, recipient_list)
    messages.success(request, "orders confirmation were succesfull")
    Order.objects.filter(author=current).delete()
    return redirect('cart')
