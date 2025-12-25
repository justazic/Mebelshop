from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.contrib import messages
from .models import Category, Product
from .forms import ProductForm,CommentForm
from django.views import View 

# Create your views here.

# def home(request):
#     categories = Category.objects.all() 
#     products = Product.objects.filter().order_by('-id')
    
#     query = request.GET.get('q')
#     if query:
#         products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
#         if len(products) == 0:
#             messages.info(request, f"{query} boyicha maxsulot topilmadi")
#             products = Product.objects.filter().order_by('-id')
#     else:
#         products = Product.objects.filter().order_by('-id')
            
#     context = {'categories': categories, 'products': products}
#     return render(request, 'home.html', context)

# def category_products(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     products = Product.objects.filter(category=category).order_by('-id')
#     context = {'category': category, 'products': products}
#     return render(request, 'category_products.html', context)

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product':product}
#     return render(request, 'product_detail.html', context)

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save() 
#             messages.success(request, 'Maxhsulot muvafaqiyatli qoshildi')
#             return redirect('home')
#     else:
#         form = ProductForm()
#     context = {'form': form} 
#     return render(request, 'product_form.html', context)


# def edit_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance =product)
#         if form.is_valid():
#             form.save() 
#             messages.success(request, 'Maxhsulot muvafaqiyatli yangilandi')
#             return redirect('home')
#     else:
#         form = ProductForm(instance=product)
#     context = {'form': form} 
#     return render(request, 'product_form.html', context)

# def delete_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete() 
#         messages.success(request, 'Mahsulot muvafaqiyatli ochirildi')
#         return redirect('home')
#     context = {'product': product}
#     return render(request, 'product_delete.html', context)

class HomeView(View):
    def get(self,request):
        categories = Category.objects.all() 
        products = Product.objects.all().order_by('id')
        
        query = request.GET.get('q')
        if query:
            products = products.filter(Q(name__icontains=query))
            if not products.exists():
                messages.info(request, f"{query} Boyicha mahsulot topilmadi")
                products = Product.objects.all().order_by('-id')
                
        context = {'categories': categories, 'products':products}
        return render(request, 'home.html', context)
    
class CategoryProductsView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category).order_by('-id')
        context = {'category':category, 'products':products}
        return render(request, 'category_products.html', context)
    
    
class ProductDetailView(View):
    def get(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        comments = product.comments.all().order_by('-created_at')
        form = CommentForm() 
        
        context = {'product': product, 'comments':comments,'form': form}
        return render(request, 'product_detail.html', context)
    
    def post(self,request, pk):
        product = get_object_or_404(Product, pk=pk)
        comments = product.comments.all().order_by('-created_at')
        form = CommentForm(request.POST, request.FILES) 
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user 
            comment.product = product
            if not comment.rate:
                comment.rate = 0
            comment.save() 
            return redirect('product_detail', pk=pk)
        
        context = {'product': product, 'comments':comments, 'form':form}
        return render(request, 'product_detail.html', context)
    
    
class ProductCreateView(View):
    def get(self, request):
        form = ProductForm() 
        return render(request, 'product_form.html', {'form': form})
    
    def post(self,request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            form.save() 
            messages.success(request, "Mahsulot muvafaqiyatli qoshildi")
            return redirect('home')
        return render(request, 'product_form.html', {'form':form})
    
    
class ProductUpdateView(View):
    def get(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product_form.html', {'form': form,'product':product})
    
    def post(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.user = product.user
            updated_product.save() 
            messages.success(request, "Mahsulot muvafaqiyatli yangilandi")
            return redirect('home')
        return render(request, 'product_form.html', {'form':form, 'product':product})
    
    
class ProductDeleteView(View):
    def get(self,request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_delete.html', {'product': product})
    
    def post(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete() 
        messages.success(request, 'Mahsulot muvafaqiyatli ochirildi')
        return redirect('home')
    