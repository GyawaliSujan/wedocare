from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        # Login USER
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credintentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
       #check if password match
        if password == password2:
            #check username (bring user model )
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This Email id is already used')
                    return redirect('register')
                else:
                   #looksGood
                    user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    # login after register
                    user.save()
                    messages.success(request, 'Successfully registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords donot match')
            return redirect('register')
    else:
      return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully Logged Out')
        return redirect('index')