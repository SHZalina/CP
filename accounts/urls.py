from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/confim', views.confirmregister, name="confirmregister"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
    path('change_password/', views.change_password, name='change_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset.html'), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_done.html'), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'), name='password_reset_complete'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/myinquiries', views.myinquiries, name="myinquiries"),
    path('dashboard/inquiry', views.inquiry1, name="inquiry1"),
]