import multiprocessing
import os
import random
import time

import django


class TaskAddManager:
    def __init__(self):
        self.process = None

    @staticmethod
    def regular_task_add():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_app.settings")
        django.setup()

        from application.models import Employee, Order
        employees = Employee.objects.all()

        def add_order_to_random_employee() -> None:
            order = Order.objects.create(name="Test Record", employee=random.choice(employees))
            order.name = order.name + f" {order.id}"
            order.save()
            print("Order added")

        # The time.sleep() function does not consider the time of operations and function calls.
        # Such a structure will provide clarity:
        # 1 order for 1 minute, several times checking changes of the current time from the operating system.

        time_point = time.time() // 60
        add_order_to_random_employee()

        while True:
            if time.time() // 60 > time_point:
                add_order_to_random_employee()
                time_point = time.time() // 60

            time.sleep(15)
            print("One Iteration")
            print(time.time() // 60, time_point)

    def start(self) -> None:
        self.process = multiprocessing.Process(target=self.regular_task_add, daemon=True)
        self.process.start()

    def is_process_alive(self) -> bool:
        return self.process.is_alive()

    def stop(self) -> None:
        if self.process:
            self.process.terminate()
            self.process = None


if __name__ == "__main__":
    task_manager = TaskAddManager()
    task_manager.start()

    time.sleep(125)

    task_manager.stop()
