from urllib.error import HTTPError

from core.groups.squad import Squad
from core.structure.base.hero import Hero


class Battlefield:
    def __init__(self, size:int):
        self.__size = max(size, 1)
        self.__s1 = Squad(self.__size)
        self.__s2 = Squad(self.__size)

    def fight(self) -> None:
        step: int = 1
        h1: Hero
        h2: Hero
        attack: int
        while self.__s1.any_alive() and self.__s2.any_alive():
            print(f"\033[33mStep: {step}\033[0m")
            h1 = self.__s1.get_hero()
            h2 = self.__s2.get_hero()
            attack = h1.make_attack()
            print(h1, "\033[43m",attack, ">>>", "\033[0m", h2)
            h2.take_damage(attack)
            print(h1, "   ", h2)
            if h1.is_alive and h2.is_alive:
                attack = h2.make_attack()
                print(h2, "\033[45m",attack, "\033[0m", "<<<", h1)
                h1.take_damage(attack)
                print(h1, "   ", h2)
            step += 1
            input()  # Продовження після натискання <Enter>

        print(f"\033[33mSquad {1 if self.__s1.any_alive() else 2} Win!\033[0m")  # Тернарний оператор на Python
        if self.__s1.any_alive():
            print("\n\033[33mSquad 1\n\033[0m", self.__s1, sep="")
        else:
            print("\n\033[33mSquad 2\n\033[0m", self.__s2, sep="")



