from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'Index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['confirm-password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request, 'User created successfully')
                return redirect('/login/')
        else:
            messages.info(request,'Password not match')
            return redirect('/register/')

    return render(request,'Register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/application/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login/')
    return render(request,'Login.html')

def account_application(request):
    return render(request,'Application.html')