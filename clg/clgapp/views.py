from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login


def function(request):
    return render(request, 'index.html')
def loginpage(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
def new(request):
    return render(request, 'new.html')
def submit(request):
    return render(request, 'submit_message.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['Name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm password']

        if password == cpassword:
            myuser = User.objects.create_user(username=username, password=password)
            myuser.save()
            messages.success(request, "account created")
            return redirect("signin")
        else:
            # messages.error(request,"password does not match")
            return redirect('signup')
    return render(request,'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'new.html')

        else:
            messages.error(request, "error")
            # return redirect("signup")
            return render(request, "register.html")
    return render(request,"login.html")


def action(request):
    return render(request, 'index.html')

# drop

def index(request):
    department = Department.objects.all()
    d = {'department': department}
    return render(request,'drop.html',d)

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})

