from django import forms
from .models import Product, Category, Comment


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
        

class CommentForm(forms.ModelForm):
    rate = forms.IntegerField(min_value=0,max_value=5, required=0)
    class Meta:
        model = Comment
        fields = ['text', 'rate', 'image_comment']
        