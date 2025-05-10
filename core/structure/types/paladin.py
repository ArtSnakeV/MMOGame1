from typing import final

from core.structure.specialities.warrior import Warrior

@final
class Paladin(Warrior):
    def __init__(self, name: str, hp: int, max_attack: int, armor: int):
        super().__init__(name, hp, max_attack, int(armor*1.7))
    def __str__(self):
        return f"\033[90mPaladin\033[0m, {super().__str__()}"
