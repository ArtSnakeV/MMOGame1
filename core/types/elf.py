from typing import final

from core.structure.specialities.archer import Archer

@final
class Elf(Archer):
    def __init__(self, name: str, hp: int, max_attack: int, arrows: int):
        super().__init__(name, hp, int(max_attack*1.4), int(arrows*1.1)) #Elf gets' extra arrows and max_attack
    def __str__(self):
        return f"\033[37mElf\033[0m, {super().__str__()}"