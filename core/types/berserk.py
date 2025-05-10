from typing import final

from core.structure.specialities.warrior import Warrior

@final
class Berserk(Warrior):
    def __init__(self, name: str, hp: int, max_attack: int, armor: int):
        super().__init__(name, int(hp*1.5), int(max_attack*1.5), armor)
    def __str__(self):
        return f"\033[91mBerserk\033[0m, {super().__str__()}"