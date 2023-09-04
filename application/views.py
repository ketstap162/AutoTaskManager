from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from application.models import Order
from application.tasks import TaskAddManager
from application.bot import TelegramBot

# Create your views here.


task_manager = TaskAddManager()


@login_required
def home_page_view(request) -> HttpResponse:
    task_add_param = request.GET.get("task_add")

    if task_add_param == "activate":
        task_manager.start()
        print("Task Add Started")
    elif task_add_param == "deactivate":
        task_manager.stop()
        print("Task Add Stopped")

    context = {
        "orders": Order.objects.select_related("employee")
    }

    if not request.user.is_superuser:
        context["orders"] = context["orders"].filter(employee=request.user)

    return render(request, "index.html", context=context)


@login_required
def delete_task_view(request, pk: int) -> HttpResponse:
    "Задача №{pk}-{task_id} під назвою {name} була опрацьована{employee} у {datetime}"
    order = Order.objects.get(id=pk)
    message = f'Task №{pk} named "{order.name}" was processed by {order.employee.name}.'
    print(message)
    order.delete()

    TelegramBot.send_message(message)

    return redirect('Application:Home')
