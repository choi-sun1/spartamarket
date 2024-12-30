from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

def index(request):
    return render(request, 'products/index.html')


def products(request):
    products = Product.objects.all()
    context = {
        "products" : products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product" : product,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm()
    context = {"form":form}
    return render(request, "products/create.html", context)

@login_required
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.author != request.user:
        return HttpResponseForbidden("수정권한이 없습니다.")
    
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid:
            product = form.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        "form":form,
        "product":product
    }
    return render(request, 'products/update.html', context)

@login_required
def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.author == request.user or request.user.is_superuser:
            product.delete()
        else:
            return HttpResponseForbidden("삭제권한이 없습니다.")
    return redirect("products:products")

@require_POST
def like(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect("products:product_detail", product.pk)
    return redirect("accounts:login")