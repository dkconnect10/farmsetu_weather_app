from django.urls import path
from .views import*




urlpatterns = [
    path('user_register/',user_register.as_view(),name='user_register'),
    path('login_user/',login_user.as_view(),name='login_user'),
    path('logout_user/',logout_user.as_view(),name='logout_user'),
]