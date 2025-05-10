from typing import final

from core.structure.specialities.mage import Mage

@final
class Wizard(Mage):
    def __init__(self, name: str, hp: int, max_attack: int, mana: int):
        super().__init__(name, hp, max_attack, int(mana*1.7))
    def __str__(self):
        return f"\033[36mWizard\033[0m, {super().__str__()}"

    def make_attack(self) -> int:
        if self.mana>0:
            self.mana-=5 # Придумати рівень зменшення
            self.hp+=5 # Придумати рівень змін
            return int(super().make_attack()*1.5)
        return super().make_attack()