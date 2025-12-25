from django.urls import path 
from .views import HomeView,CategoryProductsView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]