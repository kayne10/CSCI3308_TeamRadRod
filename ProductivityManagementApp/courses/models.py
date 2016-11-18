from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    location = models.CharField(max_length=30)
    start_day = models.CharField(max_length=25)
    end_day = models.CharField(max_length=25)
    time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title
