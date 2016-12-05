from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render, get_object_or_404
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

def detail(request, meetup_id):
	meetup = get_object_or_404(MeetUp, pk=meetup_id)
	form = CommentForm(request.POST, request.FILES)
	return render(request, 'meetups/detail.html', {'meetup':meetup, 'form':form})


def create_meetup(request):
    form = MeetUpForm(request.POST, request.FILES)
    if form.is_valid():
        meetup = form.save(commit=False)
        meetup.user = request.user
        meetup.save()
        meetups = MeetUp.objects.all()
        return render(request, 'meetups/index.html', {'meetups': meetups})
    context = {"form": form}
    return render(request, 'meetups/create_meetup.html', context)

def create_comment(request, meetup_id):
    meetups = MeetUp.objects.all()
    form = CommentForm(request.POST or None, request.FILES or None)
    meetup = get_object_or_404(MeetUp, pk=meetup_id)
    if form.is_valid():
        meetup_comments = meetup.comment_set.all()
        comment = form.save(commit=False)
        meetup_id = meetup.id
        comment.meetup = meetup
        comment.user = request.user
        comment.save()
        meetup.save()
        return render(request, 'meetups/detail.html', {'meetup':meetup, 'meetups':meetups})
    context = {
        'meetup': meetup,
        'form': form,
        'error_message':'There was an error'
    }
    return render(request, 'meetups/create_comment.html', context)
