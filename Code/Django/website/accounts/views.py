from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
                print("USER CREATED")
        else:
            messages.info(request, "Password does not match...!!")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
