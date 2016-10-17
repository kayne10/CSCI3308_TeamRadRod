from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    location = models.CharField(max_length=30)

    def __str__(self):
		return self.title
