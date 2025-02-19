from abc import ABC, abstractmethod


# Interface para notificações (DIP e OCP)
class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str):
        raise NotImplementedError


# Implementações concretas do Notifier (Herança e Polimorfismo)
class EmailNotifier(Notifier):
    def notify(self, message: str):
        print(f"[Email] {message}")


class SMSNotifier(Notifier):
    def notify(self, message: str):
        print(f"[SMS] {message}")
