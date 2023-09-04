from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

from application.forms import EmployeeForm


def redirect_to_home(request):
    return redirect("Application:Home")


def register_view(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            return redirect("Application:Home")

    else:
        form = EmployeeForm()
    return render(request, "registration/register.html", {"form": form})
