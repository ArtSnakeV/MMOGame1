from abc import ABC
from typing import final
import random
from core.structure.base.hero import Hero


class Mage(Hero): # Множинне наслідування від Hero і ABC
    def __init__(self, name: str, hp: int, max_attack: int, mana: int):
        # super() звертання до елементів батьківського класу # приклад: super().name # приклад звертання до елемента батьківського класу
        # super().__init__() виклик конструктора батьківського класу
        super().__init__(name, hp, max_attack)
        self.__mana = mana

    # @final
    # @property
    # def mana(self) -> int:
    #     return self.__mana
    #
    # @final
    # @mana.setter
    # def mana(self, mana: int)->None:
    #     self.mana = max(mana, 0)

    @property
    @final
    def mana(self) -> int:
        return self.__mana

    @mana.setter
    @final
    def mana(self, mana: int) -> None:
        self.__mana = max(mana, 0)

    def __hash__(self):
        return hash((super().__hash__(), self.mana)) # Реалізуємо hash, використовуючи батьківський клас

    def __str__(self):
        return f"\033[34mMage {super().__str__()}, mana:{self.mana}\033[39;49m" # {super().__str__()} викликаємо str із батьківського класу

    def __eq__(self, other):
        if not isinstance(other, Hero):  # Перевіряємо, чи об'єкт типу Hero
            return False
        if (self.name == other.name
                and self.hp == other.hp
                and self.max_attack == other.max_attack
                and self.is_alive
                and other.is_alive):
            if hasattr(other, 'mana'): # Checking, if we are comparing other warrior, not Hero with different class
                if self.mana == other.mana:
                    return True
        return False

    # Метод атаки
    def make_attack(self) -> int:
        if self.is_alive:
            # Перевіряємо, якщо здоров'я менше половини, то рандомно додаємо здоров'я в залежності від кількості мани
            if self.hp <self.MAX_HP/2:
                mana_health = 0
                if self.mana>0:
                    mana_health = random.randint(0, self.mana)
                    self.mana -= mana_health # Віднімаємо від мани кількість, що витратили
                    self.hp += mana_health # Додаємо здоров'я персонажу
                    return super().make_attack() # Робимо атаку, як в батьківському класі
            # Випадок, коли здоров'я багато і атакуємо з використанням мани
            mana_attack = random.randint(0, self.mana) # Змінна кількості використаної мани на атаку
            if mana_attack > 0:
                self.mana -= mana_attack # Зменшуємо ману на кількість використаної для атаки
            return random.randint(0, self.max_attack)+mana_attack # Повертаємо значення атаки з урахуванням магічного урону
        return 0


