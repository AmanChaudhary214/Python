from django.urls import path
from . import views

app_name = 'zomato_app'

urlpatterns = [
    path('dishes/', views.dish_list, name='dish_list'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('order_list/', views.order_list, name='order_list'),
    path('place_order/', views.place_order, name='place_order'),
]
