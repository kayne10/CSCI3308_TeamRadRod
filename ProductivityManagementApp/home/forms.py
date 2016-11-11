from django import forms
from django.contrib.auth.models import User
from assignments.models import Assignment
from courses.models import Course
from meetups.models import MeetUp, Comment


class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'course', 'due_date', 'is_complete']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'description', 'location', 'start_day', 'end_day']


class MeetUpForm(forms.ModelForm):

    class Meta:
        model = MeetUp
        fields = ['title', 'assignment', 'course', 'start_time', 'est_end_time', 'location']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_content']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
