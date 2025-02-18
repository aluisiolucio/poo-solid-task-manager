from datetime import datetime
from enum import Enum
from hashlib import md5


# Enum que representa o status de uma tarefa
class TaskStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    LATE = 3


# Classe que representa uma tarefa (Encapsulamento e SRP)
class Task:
    def __init__(self, title: str, description: str, deadline: datetime):
        # Atributos privados
        self.__id = md5(title.encode()).hexdigest()
        self.__title: str = title
        self.__creation_date: datetime = datetime.now()
        self.__description: str = description
        self.__deadline: datetime = deadline
        self.__completed: bool = False
        self.__status: TaskStatus = TaskStatus.PENDING

    @property  # Getter do ID
    def id(self) -> str:
        return self.__id

    @property  # Getter do título
    def title(self) -> str:
        return self.__title

    @property  # Getter do status
    def status(self) -> TaskStatus:
        if self.__completed:
            self.__status = TaskStatus.COMPLETED
        elif self.is_late():
            self.__status = TaskStatus.LATE
        else:
            self.__status = TaskStatus.PENDING

        return self.__status

    def end_task(self):
        self.__completed = True

    def is_late(self) -> bool:
        return not self.__completed and datetime.now() > self.__deadline

    def __str__(self):
        return f"\nTask: {self.__id}\nTitle: {self.__title}\nDescription: {self.__description} \
        \nCreation Date: {self.__creation_date}\nTerm: {self.__deadline}\nStatus: {self.status.name}"
