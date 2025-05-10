from random import random, choice

first = (
    "Dark", "Shadow", "Iron", "Blood", "Storm", "Fire", "Ice", "Night", "Ghost", "Dragon",
    "Silver", "Doom", "Crimson", "Frost", "Thunder"
)

second = (
    "Blade", "Fang", "Heart", "Strike", "Hunter", "Claw", "Soul", "Eye", "Born", "Rider",
    "Song", "Bane", "Fall", "Runner", "Shade"
)

def generate_name():
    return f"{choice(first)}.{choice(second)}"