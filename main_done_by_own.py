from core.structure.base.hero import Hero
from core.structure.specialities.archer import Archer
from core.structure.specialities.mage import Mage
from core.structure.specialities.warrior import Warrior
import random
import time

# OWN MAIN JUST TO TEST BEFORE ALL TEAM STARTS


print("Heros at the beginning of battle:")
w1 = Warrior('SwordMaster', 500, 100, 250)
m1 = Mage('LightingsLord', 300, 50, 400)
a1 = Archer('TomasHood', 350, 120, 7)
w2 = Warrior('ProtectionKing', 510, 120, 270)
m2 = Mage('JevelMaster', 350, 53, 380)
a2 = Archer('LeavesShadow', 370, 130, 8)
w3 = Warrior('KnightThatBite', 450, 140, 210)
m3 = Mage('FireBob', 290, 80, 430)
a3 = Archer('TinyJane', 380, 115, 10)
w4 = Warrior('ArmoredCrusader', 585, 110, 210)
m4 = Mage('ChemistFighter', 370, 30, 450)
a4 = Archer('TreesRunner', 310, 140, 10)


heroes_list = [w1, m1, a1, w2, m2, a2, w3, m3, a3, w4, m4, a4] # Список героїв

def lets_play(heroes):
    attack_counter = 1 # Counter to calculate attacks
    counter = 0
    while attack_counter<150: # Нескінченна битва
        heroes[:] = [hero for hero in heroes if hero.hp > 0]  # rebuilding our list with only alive heroes
        print(f"\r\nAttack: {attack_counter}:")
        # Check if game is on going
        # for i in range(0, len(heroes)-1):
        #     if heroes[i].hp <= 0:
        #         heroes.pop(i)
        if counter==len(heroes)-1: # Гра завершена, лишився лише один Герой, чи жодного
            for hero1 in heroes:
                if hero1.is_alive:
                    print(f"Наш переможець це {hero1}! Вітаємо!!!")
                    return
        if counter == len(heroes):
            print(f"В цій битві немає переможців.")
            return
        # If game is on going:
        # One random Hero is making attack and other one is taking damage
        protecting_hero = heroes[random.randint(0, len(heroes)-1)]
        attacking_hero = random.randint(0, len(heroes)-1)
        print(f"Герой \r\n{heroes[attacking_hero]} атакує \r\n{protecting_hero}")
        damage = heroes[attacking_hero].make_attack()
        protecting_hero.take_damage(damage) # attack
        # time.sleep(1)
        print(f"Результати атаки: \r\n{heroes[attacking_hero]}  \r\n{protecting_hero} Damage: {damage}")
        attack_counter += 1
        if not heroes[attacking_hero].is_alive:
            counter+=1
        if len(heroes) == 0:
            return


lets_play(heroes_list)

