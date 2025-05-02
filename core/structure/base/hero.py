# class Hero:

from abc import abstractproperty, abstractmethod, ABC
from random import randint
from tkinter.font import names
from typing import final, Final  # імпортуємо анотацію final
from weakref import finalize


# наслідування від класу ABC робить клас абстрактним
class Hero(ABC):
    def __init__(self, name: str, hp : int, max_attack: int):
        self.MAX_HP: Final = 500 # константи називаються великими буквами з підкресленнями
        self.name = name # self.name - властивість, що використовується як атрибут, створює атрибут __name при виклику
        self.hp = hp # присвоюємо hp в конструкторі
        self.__max_attack = max_attack
        self.__alive: bool = True

    # властивість, гетер
    # -> str анотація, яка перевіряє тип даних, який повертається з функції
    # Правильний порядок: final property
    @final
    @property
    def name(self) -> str:
        return self.__name

    # : str це анотація, яка перевіряє тип даних параметра функції
    # : None анотація, що вказує, що в функції не повинно бути return
    @final
    @name.setter # створюємо сетер
    def name(self, name: str) -> None:
        # print("Setter for `name`")
        # створення в об'єкті атрибуту __name
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    @final
    @name.deleter # створюємо deleter
    def name(self):
        del self.__name # видаляємо приватний атрибут __name

    @final
    @property
    def hp(self) -> int:
        return self.__hp

    @final
    @hp.setter
    def hp(self, hp: int) -> None:
        self.__hp = max(min(hp, self.MAX_HP), 0) # перевіряємо hp, якщо менше 0, передається 0, якщо hp більше MAX_HP, то MAX_HP
        if self.__hp <= 0:
            self.__alive = False

    @final
    @property
    def max_attack(self) -> int:
        return self.__max_attack

    @final
    @max_attack.setter
    def max_attack(self, max_attack: int) -> None:
        self.__max_attack = max(max_attack, 0)


    @final
    @property
    def is_alive(self) -> bool:
        return self.__alive


    def __eq__(self, other):
        if not isinstance(other, Hero): # Перевіряємо, чи об'єкт типу Hero
            return False
        return (self.name == other.name
                and self.hp == other.hp
                and self.max_attack == other.max_attack
                and self.is_alive
                and other.is_alive)

    def __hash__(self):
        return hash((self.name, self.hp, self.max_attack, self.is_alive))

    def __repr__(self): # функція перетворює об'єкт в рядок. Несе повну інформацію про об'єкт
        return f"Hero(name={self.name!r}, hp={self.hp}, max_attack={self.max_attack}, is_alive={self.is_alive})" # !r означає обов'язкове використання repr при виклику
    # repr для відладки str-можна показати клієнту

    def __str__(self):
        return f"{self.name}, hp:{self.hp}, {'Alive' if self.is_alive else 'Dead'}"

    # Метод отримання damage
    def take_damage(self, damage: int) -> None:
        self.hp -= max(damage, 0) # обов'язково беремо властивості (а не атрибути), щоб властивості контролювали значення

    # Метод атаки
    def make_attack(self)->int:
        if self.is_alive:
            return randint(0, self.max_attack)
        return 0




# Перевірка
# h=Hero(12)
# print(h.name) # виклик гетера, використовуючи властивість (без дужок)
# # видалення атрибуту __name
# del h.name
#










