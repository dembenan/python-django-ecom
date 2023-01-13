from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse

from store.models import Order
from store.models import Cart
from store.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'store/index.html',context={"products":products})


def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'store/detail.html',context={"product":product})

def add_to_cart(request,id):
    user = request.user
    product = get_object_or_404(Product,id= id)
    #cart = Cart.objects.get(user = user)
    cart, _ = Cart.objects.get_or_create(user = user)
    order,created  = Order.objects.get_or_create(user=user,ordered=False, product = product)
    
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity +=1
        order.save()
    return redirect(reverse('product',kwargs={"id":id}))
        
def cart(request):
    cart = get_object_or_404(Cart,user=request.user)
    return render(request,'store/cart.html',context={"orders":cart.orders.all()})

def delete_cart(request):
    #cart = request.user.cart
    if cart := request.user.cart:
        #cart.orders.all().delete()
        cart.delete()
    return redirect("index")
        