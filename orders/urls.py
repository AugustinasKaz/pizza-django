from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name="menu"),
    path('home_menu/', views.home_menu, name="home_menu"),
    path('add1/<str:food_name>/<str:food_price>', views.add1, name="add1"),
    path('add2/<str:top_name>', views.add2, name="add2"),
    path('cart/', views.cart, name="cart"),
    path('remove/<int:food_id>/<str:food_name>', views.remove, name="remove"),
    path('confirm/', views.confirm, name="confirm")
]