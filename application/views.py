from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from application.models import Order
from application.tasks import TaskAddManager

# Create your views here.


task_manager = TaskAddManager()


@login_required
def home_page_view(request):
    task_add_param = request.GET.get("task_add")

    if task_add_param == "activate":
        task_manager.start()
        print("Task Add Started")
    elif task_add_param == "deactivate":
        task_manager.stop()
        print("Task Add Stopped")

    context = {
        "orders": Order.objects.all()
    }

    if not request.user.is_superuser:
        context["orders"] = context["orders"].filter(employee=request.user)

    return render(request, "index.html", context=context)
