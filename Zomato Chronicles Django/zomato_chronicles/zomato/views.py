from django.shortcuts import render, redirect
from .models import Dish
from .forms import DishForm
from .models import Order
from .forms import OrderForm

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'zomato/dish_list.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'zomato/add_dish.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'zomato/order_list.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # Verify dish availability if needed
            order.save()
            return redirect('zomato:order_list')
    else:
        form = OrderForm()
    return render(request, 'zomato/place_order.html', {'form': form})
