from django.shortcuts import render, redirect, reverse
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_form(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('product_list'))
    ctx = {
        'form': form
    }
    return render(request, 'product/product_form.html', ctx)


def product_list(request):
    object_list = Product.objects.all()
    ctx = {
        'object_list': object_list
    }
    return render(request, 'product/product_list.html', ctx)
