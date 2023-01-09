from django.shortcuts import render,HttpResponse,get_object_or_404
from store.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'store/index.html',context={"products":products})


def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'store/detail.html',context={"product":product})