from django.urls import path, include
from django.contrib.auth import views as auth
from .views import index

app_name = 'account'

urlpatterns = [
    path('', index, name="login"),
    path('auth/logout/', auth.LogoutView.as_view(), name='logout'),
]
