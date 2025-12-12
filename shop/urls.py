from django.urls import path 
from .views import home,category_products,product_detail,add_product,edit_product,delete_product

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit/<int:pk>/', edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', delete_product, name='delete_product')
]