from django.shortcuts import render, redirect
import random
import string
from Core.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from inquiry.models import inquiry
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def random_string(string_length = 6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) 
                   for i in range(string_length))

code = random_string()

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        avatar = request.POST['avatar']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = User
        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'avatar': avatar,
            'password': password,
        }

        # валидация
        if password == password2:
            if user.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if user.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already used')
                    return redirect('register')
                else:
                    if user.objects.filter(phone=phone).exists():
                        messages.error(request, 'Phone no  is already used')
                        return redirect('register')
                    else:
                        send_mail(
                            'Account Creation Confirmation',
                            'Привет, '+ first_name + ', Код подтверждения: ' + code,
                            'mariia.poliakova.2013@gmail.com',
                            [email],
                            fail_silently=False
                        )
                        request.method = 'GET'
                        return render(request, 'accounts/confirmregister.html', context)
        else:
            messages.error(request,'passwords donot match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def confirmregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        avatar = request.POST['avatar']
        password = request.POST['password']
        confirmcode = request.POST['confirmcode']

        user = User

        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'avatar': avatar,
            'password': password,
        }

        if code == confirmcode:
            user = user.objects.create_user(
                username=username, 
                email=email, 
                password=password,  
                phone=phone, 
                first_name=first_name, 
                last_name=last_name,
                avatar = avatar)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Confirmation Code')
            return render(request, 'accounts/confirmregister.html', context)
    else:
        return redirect('register')
    
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    
@login_required
def userlogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "you are now logged out")
        return redirect('index')
    
@login_required
def myinquiries(request):
    myinquiry = inquiry.objects.all().filter(user_id=request.user.id)
    context = {
        'myinquiries': myinquiry
    }
    return render(request, 'accounts/dashboard_myinquiries.html', context)