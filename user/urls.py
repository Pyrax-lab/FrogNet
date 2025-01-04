
from django.urls import path 
from .views import UserLogin#, RegisterUser
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('register/', views.RegisterUser.as_view(), name = "register"),
    path('register/', views.register, name = "register"),
    path("profile/", views.profile, name="profile")
]