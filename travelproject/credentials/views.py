from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# login code
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invald credentials')
            return redirect('login')

    return render(request,"login.html")




# registratin function
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username alredy exist")
                return redirect("register")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email alredy exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)

                user.save();
                messages.info(request,"sucesss")
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')