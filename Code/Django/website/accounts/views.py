from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
# Create your views here.


def register(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request, "Username already taken...!!")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, "Email already taken...!!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,first_name=fname, last_name=lname)
                user.save()
                login(request, user)
                messages.info(request, "You have successfully register. Please Login.")
                return redirect('/login')
        else:
            messages.info(request, "Password does not match...!!")
            return redirect('register')

    else:
        return render(request, 'register.html')


def logout1(request):
    logout(request)
    return redirect("/")


def login1(request):

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials.")
            return redirect('login')
    else:
        return render(request, 'login.html')
