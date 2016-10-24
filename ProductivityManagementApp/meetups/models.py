from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from assignments.models import Assignment
from courses.models import Course


# Create your models here.
class MeetUp(models.Model):
    title = models.CharField(max_length=30)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    # We want to invite users to this model. Or we can show that a user created a meetup and make it public??
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title + ' - ' + self.assignment + ' - ' + self.course
