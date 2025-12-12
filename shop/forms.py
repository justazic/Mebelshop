from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'is_active', 'image']
        labels = {'name': 'Mahsulot nomi', 'category': 'Kategoriya', "price": 'Narxi', 'description': 'Tavsifi', 'is_active': 'Aktiv', 'image': 'Rasmi'}
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {'name': 'Kategoriya nomi','description': "Tavsifi"}     