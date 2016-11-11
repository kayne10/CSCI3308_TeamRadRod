from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from .models import Course
from assignments.models import Assignment
from meetups.models import MeetUp, Comment
from home.forms import CourseForm


# Create your views here.
def index(request):
    courses = Course.objects.filter(user=request.user)
    assignments = Assignment.objects.filter(user=request.user)
    meetups = MeetUp.objects.filter(user=request.user)
    context = {
    'courses':courses,
    'assignments':assignments,
    'meetups':meetups,
    }
    return render(request, 'courses/index.html', context)

def create_course(request):
    form = CourseForm(request.POST, request.FILES)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = request.user
        course.save()
        courses = Assignment.objects.filter(user=request.user)
        return render(request, 'courses/index.html', {'courses': assignments})
    context = {
        "form": form,
        }
    return render(request, 'courses/create_course.html', context)
