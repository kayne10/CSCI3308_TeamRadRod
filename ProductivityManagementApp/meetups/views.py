from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from .models import MeetUp, Comment
from assignments.models import Assignment
from courses.models import Course
from home.forms import MeetUpForm, CommentForm


# Create your views here.
def index(request):
    courses = Course.objects.filter(user=request.user)
    assignments = Assignment.objects.filter(user=request.user)
    meetups = MeetUp.objects.all()
    context = {
    'courses':courses,
    'assignments':assignments,
    'meetups':meetups,
    }
    return render(request, 'meetups/index.html', context)


def create_meetup(request):
    form = MeetUpForm(request.POST, request.FILES)
    if form.is_valid():
        meetup = form.save(commit=False)
        meetup.user = request.user
        meetup.save()
        meetups = MeetUp.objects.all()
        return render(request, 'meetups/index.html', {'meetups': meetups})
    context = {
        "form": form,
        }
    return render(request, 'meetups/create_meetup.html', context)
