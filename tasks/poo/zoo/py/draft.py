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

def Apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(animal.nome)

class Leao(Animal):
    def __init__(self) -> None:
        super().__init__("Leãonildo")

    def fazer_som(self):
        print("Seu som é: rugir")

    def mover(self) -> None:
        print("Ele anda")

    def get_nome(self) -> str:
        return self.nome
    
    def __str__(self) -> str:
        return "Leãonildo"
    
class Elefante(Animal):
    def __init__(self) -> None:
        super().__init__("Elefantilda")

    def fazer_som(self):
        print("Seu som é: trombeta")

    def mover(self):
        print("Ele anda")

    def get_nome(self) -> str:
        return self.nome
    
    def __str__(self) -> str:
        return "Elefantilda"
    
class Cobra(Animal):
    def __init__(self) -> None:
        super().__init__("Cobralino")

    def fazer_som(self) -> None:
        print("Seu som é: ssssss")

    def mover(self) -> None:
        print("Ela rasteja")

    def get_nome(self) -> str:
        return self.nome
    
    def __str__(self) -> str:
        return "Cobralino"
    
animais = [Leao(), Elefante(), Cobra()]
for a in animais:
    Apresentar(a)
    print("------")
