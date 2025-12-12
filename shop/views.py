from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.contrib import messages
from .models import Category, Product
from .forms import ProductForm,CategoryForm

# Create your views here.

def home(request):
    categories = Category.objects.all() 
    products = Product.objects.filter().order_by('-id')
    
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if len(products) == 0:
            messages.info(request, f"{query} boyicha maxsulot topilmadi")
            products = Product.objects.filter().order_by('-id')
    else:
        products = Product.objects.filter().order_by('-id')
            
    context = {'categories': categories, 'products': products}
    return render(request, 'home.html', context)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category).order_by('-id')
    context = {'category': category, 'products': products}
    return render(request, 'category_products.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product':product}
    return render(request, 'product_detail.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Maxhsulot muvafaqiyatli qoshildi')
            return redirect('home')
    else:
        form = ProductForm()
    context = {'form': form} 
    return render(request, 'product_form.html', context)


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance =product)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Maxhsulot muvafaqiyatli yangilandi')
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    context = {'form': form} 
    return render(request, 'product_form.html', context)

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete() 
        messages.success(request, 'Mahsulot muvafaqiyatli ochirildi')
        return redirect('home')
    context = {'product': product}
    return render(request, 'product_delete.html', context)
