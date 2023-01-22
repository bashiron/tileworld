from game import Weapon

# do not export
unarmed = Weapon(
    'Unarmed',
    {
        'phys': 10,
        'magc': 0,
        'lgtn': 0,
        'fire': 0
    }, 15, 999, 0
)

moonlight = Weapon(
    'Moonlight Greatsword',
    {
        'phys': 40,
        'magc': 80,
        'lgtn': 0,
        'fire': 0
    }, 20, 150, 30
)

stonecold = Weapon(
    'Stonecold Greathammer',
    {
        'phys': 110,
        'magc': 20,
        'lgtn': 0,
        'fire': 0
    }, 10, 500, 75
)

surge = Weapon(
    'Surge',
    {
        'phys': 20,
        'magc': 30,
        'lgtn': 0,
        'fire': 100
    }, 35, 300, 25
)

# -----------------------------------------
export = [moonlight, stonecold, surge]
