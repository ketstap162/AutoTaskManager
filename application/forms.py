from django import forms
from django.contrib.auth.forms import UserCreationForm

from application.models import Employee


class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ["name", "email"]
