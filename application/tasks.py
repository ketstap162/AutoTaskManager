import multiprocessing
import time


class TaskAddManager:
    def __init__(self):
        self.process = multiprocessing.Process(target=self.regular_task_add)

    @staticmethod
    def regular_task_add():
        while True:
            print("Process iteration started")
            time.sleep(2)
            print("Proces iteration ended")

    def start(self) -> None:
        self.process.start()

    def is_process_alive(self) -> bool:
        return self.process.is_alive()

    def stop(self) -> None:
        self.process.terminate()


if __name__ == "__main__":
    task_manager = TaskAddManager()
    task_manager.start()

