from typing import List
from task import Task, TaskStatus
from notifier import Notifier
from hashlib import md5


# Classe que representa um usuário com lista de tarefas (SRP e DIP)
class User:
    def __init__(self, name: str, notifier: Notifier):
        self.__id = md5(name.encode()).hexdigest()
        self.__name = name
        self.__notifier = notifier
        self.__tasks: List[Task] = []

    def add_task(self, task: Task):
        self.__tasks.append(task)
        self.__notifier.notify(f"Nova tarefa adicionada: {task.title} ({task.id})")

    def list_tasks(self):
        print("\nLista de tarefas:")
        for task in self.__tasks:
            print(task)

    def check_delayed_tasks(self):
        print("\nVerificando tarefas atrasadas:")
        for task in self.__tasks:
            if task.is_late():
                self.__notifier.notify(
                    f"Atenção! A seguinte tarefa está atrasada: {task.title} ({task.id})"
                )

    def check_completed_tasks(self):
        print("\nVerificando tarefas concluídas:")
        flag = False
        for task in self.__tasks:
            if task.status == TaskStatus.COMPLETED:
                flag = True
                self.__notifier.notify(
                    f"Parabéns! A seguinte tarefa foi concluída: {task.title} ({task.id})"
                )
            
        if not flag:
            print("Nenhuma tarefa concluída.")
