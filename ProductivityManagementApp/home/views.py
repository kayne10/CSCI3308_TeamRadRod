from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from .forms import UserForm
from courses.models import Course
from assignments.models import Assignment
from meetups.models import MeetUp, Comment


# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        courses = Course.objects.filter(user=request.user)
        assignments = Assignment.objects.filter(user=request.user)
        meetups = MeetUp.objects.filter(user=request.user)
        user = request.user
        context = {
        'courses':courses,
        'user': user,
        'assignments':assignments,
        'meetups':meetups,
        }
        return render(request, 'home/index.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # pass in all objects
                return render(request, 'home/index.html')
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'home/index.html')
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login.html', context)
