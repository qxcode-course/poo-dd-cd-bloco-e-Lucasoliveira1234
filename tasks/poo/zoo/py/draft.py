from typing import Any
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def apresentar_nome(self):
        print(f"O animal é {self.nome}")

    @abstractmethod
    def fazer_som(self) -> None:
        pass

    @abstractmethod
    def mover(self) -> None:
        pass

class Leao(Animal):
    pass
