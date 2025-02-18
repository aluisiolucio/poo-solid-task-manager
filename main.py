from datetime import datetime
from task import Task
from user import User
from notifier import EmailNotifier


def main():
    email_notifier = EmailNotifier()
    user = User("Aluisio", email_notifier)

    task1 = Task(
        "Estudar SOLID",
        "Revisar conceitos e implementar exemplos",
        datetime(2025, 2, 20),
    )
    task2 = Task("Estudar Python", "Ler livro sobre Python", datetime(2025, 2, 10))
    task3 = Task("Estudar Java", "Ler livro sobre Java", datetime(2025, 2, 15))

    user.add_task(task1)
    user.add_task(task2)
    user.add_task(task3)

    user.list_tasks()

    user.check_delayed_tasks()

    task1.end_task()
    user.check_completed_tasks()


if __name__ == "__main__":
    main()
