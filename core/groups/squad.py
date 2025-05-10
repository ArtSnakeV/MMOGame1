from random import randint, choice

from core.groups.name_generator import generate_name
from core.structure.hero_types import Types
from core.structure.types.berserk import Berserk
from core.structure.types.elf import Elf
from core.structure.types.hunter import Hunter
from core.structure.types.paladin import Paladin
from core.structure.types.warlock import Warlock
from core.structure.types.wizard import Wizard


class Squad:
    def __init__(self, size: int): # size-size of squad
        self.__size = max(size, 1)
        self.__heroes = [] # Можна і list(), але швидше через []
        self.__fill() # Метод для заповнення списку героями

    def __fill(self):
        for _ in range(self.__size):
            # hero: Hero = None
            # hero = None
            match choice(tuple(Types)):
                case Types.PALADIN:
                    hero = Paladin(generate_name(), randint(100, 200), randint(30, 70), 40)
                case Types.BERSERK:
                    hero = Berserk(generate_name(), randint(100, 200), randint(30, 70), 30)
                case Types.WIZARD:
                    hero = Wizard(generate_name(), randint(100, 200), randint(30, 70), 50)
                case Types.WARLOCK:
                    hero = Warlock(generate_name(), randint(100, 200), randint(30,50), 80)
                case Types.HUNTER:
                    hero = Hunter(generate_name(), randint(100, 200), randint(30,50), randint(5,10))
                case Types.ELF:
                    hero = Elf(generate_name(), randint(100, 200), randint(30, 50), randint(5, 10))
                # Add other types of heroes


                case _: # default `case`
                    raise ValueError("Wrong value (while choosing hero type)")

            self.__heroes.append(hero)

    def __str__(self):
        return "\n".join(str(hero) for hero in self.__heroes ) # str(hero) щоб уникнути помилку, якщо герой `None`

    def any_alive(self):
        return any(hero.is_alive for hero in self.__heroes) # якщо хоча б одне значення True, використовуємо ф-цію any()

    def get_hero(self):
        # Робимо генератор
        alive_heroes = [hero for hero in self.__heroes if hero.is_alive]
        # alive_heroes = tuple(hero for hero in self.__heroes if hero.is_alive) # створюємо кортеж з усіма героями
        # alive_heroes = tuple(filter(lambda a : a.is_alive(), self.__heroes))
        if not alive_heroes:
            raise ValueError("No any alive")
        return choice(alive_heroes)
