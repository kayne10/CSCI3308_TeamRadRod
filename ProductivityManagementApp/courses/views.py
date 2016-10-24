from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from .models import Course


# Create your views here.
def index(request):
    all_courses = Course.objects.all()
    context = {
    'all_courses':all_courses,
    }
    return render(request, 'courses/index.html', {'context':context})
