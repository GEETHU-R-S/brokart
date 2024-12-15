from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_product=Product.objects.order_by('-priority')[:4]
    latest_product=Product.objects.order_by('-id')[:4]
    context={
        'featured_product':featured_product,
        'latest_product':latest_product

    }

    return render(request,'index.html',context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={'Product':product_list}

    return render(request,'products.html',context)

def detail_products(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}

    return render(request,'product_detail.html',context)