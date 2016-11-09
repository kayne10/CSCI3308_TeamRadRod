from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from courses.models import Course

# Create your models here.
class Assignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now=False)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
