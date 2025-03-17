from django.shortcuts import render
from .models import *
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/Store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        # ^NEeds to be handled later

    context = {'items':items}
    return render(request, 'store/Cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/Checkout.html', context)
