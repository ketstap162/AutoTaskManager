from django.http import HttpResponse
from django.shortcuts import render

from application.tasks import TaskAddManager

# Create your views here.


task_manager = TaskAddManager()


def home_page_view(request):
    task_add_param = request.GET.get("task_add")

    if task_add_param == "activate":
        task_manager.start()
        print("Task Add Started")
    elif task_add_param == "deactivate":
        task_manager.stop()
        print("Task Add Stopped")

    response_string = "200 - OK"

    return HttpResponse(response_string)
