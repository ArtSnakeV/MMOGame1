from abc import ABC
from typing import final
from core.structure.base.hero import Hero


class Warrior(Hero): # Множинне наслідування від Hero і ABC
    def __init__(self, name: str, hp: int, max_attack: int, armor: int):
        # super() звертання до елементів батьківського класу # приклад: super().name # приклад звертання до елемента батьківського класу
        # super().__init__() виклик конструктора батьківського класу
        super().__init__(name, hp, max_attack)
        self.armor = armor

    @final
    @property
    def armor(self) -> int:
        return self.__armor

    @final
    @armor.setter
    def armor(self, armor: int)->None:
        self.__armor = max(armor, 0)

    def __eq__(self, other):
        if not isinstance(other, Hero):  # Перевіряємо, чи об'єкт типу Hero
            return False
        if (self.name == other.name
                and self.hp == other.hp
                and self.max_attack == other.max_attack
                and self.is_alive
                and other.is_alive):
            if hasattr(other, 'armor'): # Checking, if we are comparing other warrior, not Hero with different class
                if self.armor == other.armor:
                    return True
        return False

    def __hash__(self):
        return hash((super().__hash__(), self.armor)) # Приклад реалізації hash, використовуючи батьківський клас

    def __str__(self):
        return f"\033[31mWarrior {super().__str__()}, armor:{self.armor}\033[39;49m" # {super().__str__()} викликаємо str із батьківського класу

    def take_damage(self, damage: int) -> None:
        if damage > self.armor > 0:
            self.armor -= damage
            return
        else:
            if self.armor>0:
                damage_effective = damage - self.armor
                self.armor = 0  # зменшення броні
                super().take_damage(damage_effective)
                return
        super().take_damage(damage)


    def make_attack(self) ->int:
        return super().make_attack()