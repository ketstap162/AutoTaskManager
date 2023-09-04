import multiprocessing
import os
import time

import django


class TaskAddManager:
    def __init__(self):
        self.process = None

    @staticmethod
    def regular_task_add():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_app.settings")
        django.setup()

        from application.models import Employee
        employees = Employee.objects.all()

        with open("employees.txt", "a") as file:
            for employee in employees:
                file.write(str(employee) + "\n")

    def start(self) -> None:
        self.process = multiprocessing.Process(target=self.regular_task_add, daemon=True)
        self.process.start()

    def is_process_alive(self) -> bool:
        return self.process.is_alive()

    def stop(self) -> None:
        self.process.terminate()


if __name__ == "__main__":
    task_manager = TaskAddManager()
    task_manager.start()

    time.sleep(10)

    task_manager.stop()
