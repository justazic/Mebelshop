from django.urls import path 
from .views import RegisterView,LoginView,LogoutView,ProfileView,ChangePaswordView,EditProfileView,EditComentView,DeleteCommentView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('pasword/change/', ChangePaswordView.as_view(), name='change_password'),
    path('comment/<int:pk>/edit/', EditComentView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]