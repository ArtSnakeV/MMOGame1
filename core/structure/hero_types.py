from enum import Enum, auto, IntEnum


# Для створення enum потрібно унаслідувати клас від класу Enum або IntEnum
class Types(Enum):
    BERSERK="Berserk",
    PALADIN="Paladin",
    WIZARD="Wizard",
    WARLOCK="Warlock",
    ELF="Elf",
    HUNTER="Hunter", # Після констант ставимо кому, і після останньої теж ставимо кому

# Приклад генерації `IntEnum`-а
class TestIntEnum(IntEnum):
    A=0,
    # Для автоматичного генерування номерів
    B=auto() # auto для того, щоб номера генерувалися автоматично














# І імпорті пакет має приорітет, тому файл не називається `types`
