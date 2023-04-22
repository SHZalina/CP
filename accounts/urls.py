from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/confim', views.confirmregister, name="confirmregister"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
]