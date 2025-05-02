from abc import ABC
from typing import final
import random
from core.structure.base.hero import Hero


class Archer(Hero): # Множинне наслідування від Hero і ABC
    def __init__(self, name: str, hp: int, max_attack: int, arrows: int):
        # super() звертання до елементів батьківського класу # приклад: super().name # приклад звертання до елемента батьківського класу
        # super().__init__() виклик конструктора батьківського класу
        super().__init__(name, hp, max_attack)
        self.__arrows = arrows

    @property
    @final
    def arrows(self) -> int:
        return self.__arrows

    @arrows.setter
    @final
    def arrows(self, arrows: int)->None:
        self.__arrows = max(arrows, 0)

    def __hash__(self):
        return hash((super().__hash__(), self.arrows)) # Реалізуємо hash, використовуючи батьківський клас

    def __str__(self):
        return f"\033[32mArcher {super().__str__()}, arrows:{self.arrows}\033[39;49m" # {super().__str__()} викликаємо str із батьківського класу

    def __eq__(self, other):
        if not isinstance(other, Hero):  # Перевіряємо, чи об'єкт типу Hero
            return False
        if (self.name == other.name
                and self.hp == other.hp
                and self.max_attack == other.max_attack
                and self.is_alive
                and other.is_alive):
            if hasattr(other, 'arrows'): # Checking, if we are comparing other warrior, not Hero with different class
                if self.arrows == other.arrows:
                    return True
        return False

    # Метод атаки
    def make_attack(self) -> int:
        if self.is_alive:
            # Перевіряємо, якщо у лучника є стріли
            if self.arrows >0:
                # У нас дуже професійний лучник він може стріляти 1, 2-ма чи 3-ма стрілами
                arrows_amount = 1
                # Якщо стріл більше 2-х, то наш досвічений лучник може зробити постріл 1-ю, 2-ма, чи 3-ма стрілами
                if arrows_amount > 2:
                    arrows_amount = random.randint(1, 3) # може і взагалі промазати і пропустити час атаки

                    print("here")
                self.arrows -= arrows_amount # Віднімаємо витрачені стріли
                return super().make_attack()*arrows_amount # використовуємо батьківський клас для підрахування атаки
        return 0 # Якщо стріл немає

