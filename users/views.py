from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm


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
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile.html', {'form': form})
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Profil Yangilandi!')
            return redirect('profile')
        return render(request, 'users/profile.html', {'form': form})
    