from core.helper import AttrDict


class PlayerTuning(object):
    JUMP_WINDOW = 32

    STARTING_ITEMS = [
        # Example: ('item_name', 1)
    ]

    STARTING_RECIPES = [
        "lumber",
        "paper",
        "torch",
        "research_desk",
        "makeshift_tool",
        "wood_club"
    ]

    LEVEL_EXPERIENCE_REQUIRED = [250, 300, 350, 400, 450, 500, 550, 600, 650, 750, 850, 950] + [1000] * 32 + [1100, 1200, 1300, 1400, 1500, 1500] + [1500] * 20 + [1600] * 15 + [1700] * 10 + [1800, 1850, 1900, 1950, 2000]

    STATS = AttrDict(
        HP=100,
        SP=100,
        ATK=5,
        DEF=5,
        INT=5,
        MIND=5,
        AGI=5,
        LUCK=5,
        fire=100,
        water=100,
        earth=100,
        wind=100
    )

    LEVEL_STATS = [
        AttrDict(level=1, HP=3, SP=0, ATK=1, DEF=1, INT=1, MIND=1, AGI=1, LUCK=0),
        AttrDict(level=6, HP=4, SP=0, ATK=1, DEF=1, INT=1, MIND=1, AGI=1, LUCK=0),
        AttrDict(level=11, HP=5, SP=0, ATK=1, DEF=1, INT=1, MIND=1, AGI=1, LUCK=0),
        AttrDict(level=16, HP=6, SP=0, ATK=2, DEF=2, INT=2, MIND=2, AGI=2, LUCK=0),
        AttrDict(level=21, HP=7, SP=0, ATK=2, DEF=2, INT=2, MIND=2, AGI=2, LUCK=0),
        AttrDict(level=26, HP=8, SP=0, ATK=3, DEF=3, INT=2, MIND=2, AGI=2, LUCK=0),
        AttrDict(level=31, HP=9, SP=0, ATK=3, DEF=3, INT=3, MIND=3, AGI=3, LUCK=0),
        AttrDict(level=36, HP=10, SP=0, ATK=3, DEF=3, INT=3, MIND=3, AGI=3, LUCK=0),
        AttrDict(level=41, HP=11, SP=0, ATK=4, DEF=4, INT=4, MIND=4, AGI=4, LUCK=0),
        AttrDict(level=46, HP=12, SP=0, ATK=4, DEF=4, INT=4, MIND=4, AGI=4, LUCK=0)
    ]

    CRAFT_CATALYSTS_AMOUNT = 5

    # Maximum number of total infusions per level
    INFUSIONS_PER_LEVEL = 3
    # Number of infusions gained per level (player can immediately spend)
    INFUSIONS_GAINED_PER_LEVEL = 2
    # Individual maximums for infusions per level
    INFUSION_STAT_PER_LEVEL = {
        'HP': 2,
        'SP': 2,
        'ATK': 2,
        'DEF': 2,
        'INT': 2,
        'MIND': 2,
        'AGI': 2,
        'LUCK': 1
    }
    # How much of to raise a stat when infused
    INFUSION_STAT_INCREASE_PER_LEVEL = {
        'HP': 3,
        'SP': 2,
        'ATK': 1,
        'DEF': 1,
        'INT': 1,
        'MIND': 1,
        'AGI': 1,
        'LUCK': 1
    }

    STARTING_BAG_SIZE = 25
    BAG_SIZE_ICON = {
        10: 'mods/core/ui/images/inventory/pouch.png',
        15: 'mods/core/ui/images/inventory/satchel.png',
        20: 'mods/core/ui/images/inventory/bag.png',
        25: 'mods/core/ui/images/inventory/pack.png',
    }

    CHOP_COOLDOWN = 900
    DIG_COOLDOWN = 600
    MAX_COMBOS = [2, 2, 3, 3, 3]
