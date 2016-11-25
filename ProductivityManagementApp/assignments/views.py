from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from .models import Assignment
from courses.models import Course
from meetups.models import MeetUp, Comment
from home.forms import AssignmentForm


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
    return render(request, 'assignments/index.html', context)

def create_assignment(request):
    form = AssignmentForm(request.POST, request.FILES)
    if form.is_valid():
        assignment = form.save(commit=False)
        assignment.user = request.user
        assignment.save()
        assignments = Assignment.objects.filter(user=request.user)
        return render(request, 'assignments/index.html', {'assignments':assignments})
    context = {
        "form": form,
        }
    return render(request, 'assignments/create_assignment.html', context)
