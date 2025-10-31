from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user_profile, name='user'),
    path('sale/', views.sale, name='sale'),
    path('profile/<str:username>/', views.user_profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('add_property/', views.add_property, name='add_property'),
]
