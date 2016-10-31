from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from .models import MeetUp, Comment
from assignments.models import Assignment
from courses.models import Course


# Create your views here.
def index(request):
    courses = Course.objects.all()
    assignments = Assignment.objects.all()
    meetups = MeetUp.objects.all()
    context = {
    'courses':courses,
    'assignments':assignments,
    'meetups':meetups,
    }
    return render(request, 'meetups/index.html', context)
