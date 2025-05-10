from random import randint
from typing import final

from core.structure.specialities.mage import Mage

# поки є мана, понижує здоров'я, щоб сильно збільшити атаку,
# коли мана закінчується,- просто атакує
@final
class Warlock(Mage):
    def __init__(self, name: str, hp: int, max_attack: int, mana: int):
        super().__init__(name, hp, max_attack, int(mana*1.1))
    def __str__(self):
        return f"\033[35mWarlock\033[0m, {super().__str__()}"

    def make_attack(self) -> int:
        if self.mana>0 and self.hp>10: # Також перевіряємо рівень здоров'я, щоб варлок не знищив себе
            mana_improvements: 1 # Variable to get value of attack improvement coefficient depending on mana amount
            if self.mana > 10:
                mana_improvements = int(self.mana/(randint(2,5))) # Will reduce gradually
                self.mana -= mana_improvements
            else:
                mana_improvements = self.mana
                self.mana = 0
            self.hp-= int(mana_improvements/3) # Придумати рівень змін
            return int(super().make_attack()+mana_improvements)
        return super().make_attack()