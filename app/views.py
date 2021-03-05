from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from app.models import data
from django.core.mail import send_mail



def Home(request):
    return render(request, 'index.html')

def Resume(request):
    return render(request, "resume.html")


def Project1(request):
    return render(request,"project1.html")

def Project2(request):
    return render(request,"project2.html")

def Project3(request):
    return render(request,"AI_assistant.html")

def Signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1!=password2:
            messages.error(request, 'Passwords Does Not Match')
        



        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Exists Try Different Username")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered Use Another Email")
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save();
                messages.info(request, "Account Successfully Created")
        
    return render(request,'signup.html')

def build(request):
    if request.user.is_anonymous:
        return redirect('Signup')
    return render(request, 'coming.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('build')
        else:
            return render(request, "login.html")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')


def Feedback(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        femail=request.POST["femail"]
        fmessage=request.POST["fmessage"]
        m = messages.info(request, "Thank you for Contacting us"+" "+fname)


        send_mail(
            fname,
            fmessage,
            femail,
            ["mshukla376@gmail.com"]
        )
        return render(request, "feedback.html")

    return render(request, "feedback.html")

def Blog(request):
    return render(request,"blog.html")


