from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from shop.models import Product, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm() 
        return render(request, 'users/register.html', {'form':form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            messages.success(request, 'Royxatdan Muvafaqiyatli otdingiz!')
            return redirect('home')
        return render(request, 'users/register.html', {'form': form})
    
    
class LoginView(View):
    def get(self,request):
        form = AuthenticationForm() 
        return render(request, 'users/login.html', {'form':form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request, user)
            return redirect('home')
        return render(request,'users/login.html', {'form':form})
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')
    
    
class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        user_products = Product.objects.filter(user=request.user).order_by('-id')
        user_products_count = user_products.count()
        user_comments = Comment.objects.filter(user=request.user).order_by('-created_at')
        context = {'user_products': user_products,'user_products_count': user_products_count,'user_comments': user_comments,}
        return render(request, 'users/profile.html', context)
    
    def post(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if request.FILES.get('image'):
            user = request.user
            user.image = request.FILES.get('image')
            user.save()
            messages.success(request, "Profil rasmi yangilandi!")
        
        return redirect('profile')

class EditProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = UserUpdateForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = UserUpdateForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profil muvaffaqiyatli yangilandi")
            return redirect('profile')

        return render(request, 'users/edit_profile.html', {'form': form})


class ChangePaswordView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = PasswordChangeForm(user=request.user)
        return render(request, 'users/change_pass.html', {'form':form})
    
    def post(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save() 
            update_session_auth_hash(request, user)
            messages.success(request, 'Parol muvafaqiyatli ozgartirildi')
            return redirect('profile')
        return render(request, 'users/change_pass.html', {'form':form})
    
    
class EditComentView(LoginRequiredMixin,View):
    def get(self,request,pk):
        comment = get_object_or_404(Comment, pk=pk, user=request.user)
        return render(request, 'edit_comment.html', {'comment':comment})
    
    def post(self,request,pk):
        comment = get_object_or_404(Comment, pk=pk, user=request.user) 
        new_text = request.POST.get('text')
        
        if new_text:
            comment.text = new_text
            comment.save() 
            messages.success(request, "Comment muvafaqiyatli yangilandi")
            return redirect('profile')
        return render(request, 'edit_comment.html',{'comment':comment})
    
    
class DeleteCommentView(LoginRequiredMixin,View):
    def get(self,request,pk):
        comment = get_object_or_404(Comment, pk=pk, user=request.user) 
        comment.delete() 
        messages.success(request, 'Comment muvafaqiyatli ochirildi')
        return redirect('profile')