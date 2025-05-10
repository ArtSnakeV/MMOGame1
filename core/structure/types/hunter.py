from typing import final

from core.structure.specialities.archer import Archer

@final
class Hunter(Archer):
    def __init__(self, name: str, hp: int, max_attack: int, arrows: int):
        super().__init__(name, int(hp*1.4), max_attack, int(arrows*1.3)) #Hunter gets' extra arrows and hp
    def __str__(self):
        return f"\033[93mHunter\033[0m, {super().__str__()}"