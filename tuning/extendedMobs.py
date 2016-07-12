from core.tuning.monster import MonsterTuning, SpawnerTuning
from core.tuning.animal import AnimalTuning
from core.helper import AttrDict
from siege.log import Log


def extendMobs():
    extendAnimals()

    extendAmone()
    extendGlowBat()
    extendCortess()
    extendAegnite()
    extendCenfen()
    extendEltret()
    extendHarvester()
    extendLanteed()
    extendOilSlime()
    extendOrtomi()
    extendQuaridin()
    extendIferos()
    extendStegara()
    extendMisc()
    extendTelin()
    extendTorrend()
    extendTenebrass()
    extendZabis()
    extendVenfear()
    extendBosses()
    extendSpawners()


def extendAnimals():
    new_stats = [
        AttrDict(level=51, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=56, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=61, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=66, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=71, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=76, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=81, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=86, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=91, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0),
        AttrDict(level=96, HP=20, SP=6, ATK=7, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0)
    ]

    AnimalTuning.BIRD.LEVEL_STATS = AnimalTuning.BIRD.LEVEL_STATS + new_stats
    AnimalTuning.CRAB.LEVEL_STATS = AnimalTuning.CRAB.LEVEL_STATS + new_stats
    AnimalTuning.FISH.LEVEL_STATS = AnimalTuning.FISH.LEVEL_STATS + new_stats
    AnimalTuning.SPEEP.LEVEL_STATS = AnimalTuning.SPEEP.LEVEL_STATS + new_stats
    AnimalTuning.SNOW_HARE.LEVEL_STATS = AnimalTuning.SNOW_HARE.LEVEL_STATS + new_stats


def extendAmone():
    stats = MonsterTuning.AMONE.LEVEL_STATS
    # AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=11, INT=7, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=35, SP=6, ATK=8, DEF=13, INT=8, MIND=13, AGI=7, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=8, DEF=15, INT=8, MIND=17, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=40, SP=7, ATK=9, DEF=17, INT=9, MIND=17, AGI=8, LUCK=0))
    stats.append(AttrDict(level=66, HP=45, SP=8, ATK=10, DEF=19, INT=9, MIND=19, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=45, SP=8, ATK=11, DEF=22, INT=10, MIND=22, AGI=9, LUCK=0))
    stats.append(AttrDict(level=76, HP=50, SP=9, ATK=13, DEF=24, INT=11, MIND=24, AGI=9, LUCK=0))
    stats.append(AttrDict(level=81, HP=55, SP=10, ATK=15, DEF=26, INT=12, MIND=26, AGI=10, LUCK=0))
    stats.append(AttrDict(level=86, HP=80, SP=11, ATK=17, DEF=28, INT=13, MIND=28, AGI=11, LUCK=0))
    stats.append(AttrDict(level=91, HP=120, SP=12, ATK=20, DEF=30, INT=14, MIND=30, AGI=12, LUCK=0))
    stats.append(AttrDict(level=96, HP=150, SP=13, ATK=25, DEF=35, INT=16, MIND=35, AGI=13, LUCK=0))


def extendGlowBat():
    stats = MonsterTuning.GLOW_BAT.LEVEL_STATS
    # AttrDict(level=46, HP=30, SP=6, ATK=7, DEF=10, INT=7, MIND=10, AGI=8, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=11, INT=9, MIND=11, AGI=8, LUCK=0))
    stats.append(AttrDict(level=56, HP=30, SP=7, ATK=7, DEF=12, INT=11, MIND=12, AGI=9, LUCK=0))
    stats.append(AttrDict(level=61, HP=35, SP=7, ATK=8, DEF=14, INT=13, MIND=14, AGI=9, LUCK=0))
    stats.append(AttrDict(level=66, HP=40, SP=8, ATK=8, DEF=16, INT=15, MIND=16, AGI=10, LUCK=0))
    stats.append(AttrDict(level=71, HP=45, SP=8, ATK=9, DEF=18, INT=17, MIND=18, AGI=10, LUCK=0))
    stats.append(AttrDict(level=76, HP=50, SP=9, ATK=9, DEF=20, INT=20, MIND=20, AGI=11, LUCK=0))
    stats.append(AttrDict(level=81, HP=55, SP=10, ATK=10, DEF=22, INT=22, MIND=22, AGI=12, LUCK=0))
    stats.append(AttrDict(level=86, HP=60, SP=11, ATK=11, DEF=24, INT=24, MIND=24, AGI=13, LUCK=0))
    stats.append(AttrDict(level=91, HP=80, SP=12, ATK=12, DEF=26, INT=26, MIND=26, AGI=14, LUCK=0))
    stats.append(AttrDict(level=96, HP=100, SP=13, ATK=12, DEF=28, INT=30, MIND=28, AGI=15, LUCK=0))


def extendCortess():
    stats = MonsterTuning.CORTESS.LEVEL_STATS
    # AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=12, INT=8, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=13, INT=10, MIND=13, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=7, DEF=15, INT=12, MIND=15, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=50, SP=7, ATK=8, DEF=17, INT=14, MIND=17, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=60, SP=8, ATK=8, DEF=19, INT=16, MIND=19, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=70, SP=8, ATK=9, DEF=21, INT=18, MIND=21, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=80, SP=9, ATK=9, DEF=23, INT=20, MIND=23, AGI=8, LUCK=0))
    stats.append(AttrDict(level=81, HP=90, SP=10, ATK=10, DEF=25, INT=22, MIND=25, AGI=9, LUCK=0))
    stats.append(AttrDict(level=86, HP=100, SP=11, ATK=11, DEF=27, INT=24, MIND=27, AGI=9, LUCK=0))
    stats.append(AttrDict(level=91, HP=120, SP=12, ATK=12, DEF=30, INT=26, MIND=30, AGI=10, LUCK=0))
    stats.append(AttrDict(level=96, HP=150, SP=13, ATK=12, DEF=35, INT=30, MIND=35, AGI=10, LUCK=0))

    stats = MonsterTuning.PARAGON_CORTESS.LEVEL_STATS
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=13, INT=10, MIND=13, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=50, SP=7, ATK=7, DEF=15, INT=13, MIND=15, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=70, SP=7, ATK=8, DEF=17, INT=16, MIND=17, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=90, SP=8, ATK=8, DEF=19, INT=18, MIND=19, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=110, SP=8, ATK=9, DEF=21, INT=20, MIND=21, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=130, SP=9, ATK=9, DEF=23, INT=22, MIND=23, AGI=8, LUCK=0))
    stats.append(AttrDict(level=81, HP=150, SP=10, ATK=10, DEF=25, INT=24, MIND=25, AGI=9, LUCK=0))
    stats.append(AttrDict(level=86, HP=180, SP=11, ATK=11, DEF=30, INT=26, MIND=30, AGI=9, LUCK=0))
    stats.append(AttrDict(level=91, HP=210, SP=12, ATK=12, DEF=35, INT=30, MIND=35, AGI=10, LUCK=0))
    stats.append(AttrDict(level=96, HP=250, SP=13, ATK=12, DEF=40, INT=35, MIND=40, AGI=10, LUCK=0))


def extendAegnite():
    stats = MonsterTuning.AEGNITE.LEVEL_STATS
    # AttrDict(level=46, HP=30, SP=6, ATK=7, DEF=9, INT=9, MIND=8, AGI=9, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=13, INT=10, MIND=11, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=7, DEF=15, INT=12, MIND=13, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=50, SP=7, ATK=8, DEF=17, INT=14, MIND=15, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=60, SP=8, ATK=8, DEF=19, INT=16, MIND=17, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=70, SP=8, ATK=9, DEF=21, INT=18, MIND=19, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=80, SP=9, ATK=9, DEF=23, INT=20, MIND=21, AGI=8, LUCK=0))
    stats.append(AttrDict(level=81, HP=90, SP=10, ATK=10, DEF=25, INT=22, MIND=23, AGI=9, LUCK=0))
    stats.append(AttrDict(level=86, HP=100, SP=11, ATK=11, DEF=27, INT=24, MIND=25, AGI=9, LUCK=0))
    stats.append(AttrDict(level=91, HP=120, SP=12, ATK=12, DEF=30, INT=26, MIND=30, AGI=10, LUCK=0))
    stats.append(AttrDict(level=96, HP=150, SP=13, ATK=12, DEF=35, INT=30, MIND=35, AGI=10, LUCK=0))

    stats = MonsterTuning.PARAGON_AEGNITE.LEVEL_STATS
    # AttrDict(level=46, HP=30, SP=6, ATK=7, DEF=9, INT=9, MIND=8, AGI=9, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=13, INT=10, MIND=11, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=50, SP=7, ATK=7, DEF=15, INT=13, MIND=13, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=70, SP=7, ATK=8, DEF=17, INT=16, MIND=15, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=90, SP=8, ATK=8, DEF=19, INT=18, MIND=17, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=110, SP=8, ATK=9, DEF=21, INT=20, MIND=19, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=130, SP=9, ATK=9, DEF=23, INT=22, MIND=21, AGI=8, LUCK=0))
    stats.append(AttrDict(level=81, HP=150, SP=10, ATK=10, DEF=25, INT=24, MIND=23, AGI=9, LUCK=0))
    stats.append(AttrDict(level=86, HP=180, SP=11, ATK=11, DEF=30, INT=26, MIND=25, AGI=9, LUCK=0))
    stats.append(AttrDict(level=91, HP=210, SP=12, ATK=12, DEF=35, INT=30, MIND=30, AGI=10, LUCK=0))
    stats.append(AttrDict(level=96, HP=250, SP=13, ATK=12, DEF=40, INT=35, MIND=35, AGI=10, LUCK=0))


def extendCenfen():
    stats = MonsterTuning.CENFEN.LEVEL_STATS
    # AttrDict(level=46, HP=30, SP=6, ATK=7, DEF=9, INT=9, MIND=8, AGI=9, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=11, INT=9, MIND=8, AGI=9, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=7, DEF=12, INT=10, MIND=9, AGI=10, LUCK=0))
    stats.append(AttrDict(level=61, HP=50, SP=7, ATK=8, DEF=13, INT=10, MIND=9, AGI=10, LUCK=0))
    stats.append(AttrDict(level=66, HP=60, SP=8, ATK=8, DEF=14, INT=11, MIND=10, AGI=11, LUCK=0))
    stats.append(AttrDict(level=71, HP=70, SP=8, ATK=9, DEF=15, INT=11, MIND=10, AGI=11, LUCK=0))
    stats.append(AttrDict(level=76, HP=80, SP=9, ATK=9, DEF=16, INT=12, MIND=11, AGI=12, LUCK=0))
    stats.append(AttrDict(level=81, HP=90, SP=10, ATK=10, DEF=17, INT=12, MIND=11, AGI=13, LUCK=0))
    stats.append(AttrDict(level=86, HP=100, SP=11, ATK=11, DEF=18, INT=13, MIND=12, AGI=14, LUCK=0))
    stats.append(AttrDict(level=91, HP=120, SP=12, ATK=13, DEF=20, INT=14, MIND=13, AGI=15, LUCK=0))
    stats.append(AttrDict(level=96, HP=150, SP=13, ATK=15, DEF=22, INT=15, MIND=14, AGI=16, LUCK=0))


def extendEltret():
    stats = MonsterTuning.ELTRET.LEVEL_STATS
    # AttrDict(level=46, HP=30, SP=6, ATK=7, DEF=9, INT=9, MIND=8, AGI=9, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=9, INT=9, MIND=8, AGI=9, LUCK=0))
    stats.append(AttrDict(level=56, HP=35, SP=7, ATK=7, DEF=9, INT=10, MIND=9, AGI=10, LUCK=0))
    stats.append(AttrDict(level=61, HP=30, SP=7, ATK=8, DEF=10, INT=10, MIND=9, AGI=10, LUCK=0))
    stats.append(AttrDict(level=66, HP=40, SP=8, ATK=8, DEF=10, INT=11, MIND=10, AGI=11, LUCK=0))
    stats.append(AttrDict(level=71, HP=35, SP=8, ATK=9, DEF=11, INT=11, MIND=10, AGI=11, LUCK=0))
    stats.append(AttrDict(level=76, HP=45, SP=9, ATK=9, DEF=13, INT=12, MIND=11, AGI=12, LUCK=0))
    stats.append(AttrDict(level=81, HP=55, SP=10, ATK=10, DEF=15, INT=12, MIND=13, AGI=13, LUCK=0))
    stats.append(AttrDict(level=86, HP=70, SP=11, ATK=11, DEF=17, INT=13, MIND=15, AGI=14, LUCK=0))
    stats.append(AttrDict(level=91, HP=90, SP=12, ATK=13, DEF=19, INT=14, MIND=17, AGI=15, LUCK=0))
    stats.append(AttrDict(level=96, HP=110, SP=13, ATK=15, DEF=22, INT=15, MIND=19, AGI=16, LUCK=0))


def extendHarvester():
    stats = MonsterTuning.HARVESTER.LEVEL_STATS
    # AttrDict(level=46, HP=35, SP=6, ATK=10, DEF=10, INT=7, MIND=9, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=40, SP=6, ATK=10, DEF=9, INT=7, MIND=8, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=45, SP=7, ATK=11, DEF=11, INT=8, MIND=9, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=50, SP=7, ATK=11, DEF=10, INT=8, MIND=9, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=60, SP=8, ATK=12, DEF=11, INT=9, MIND=10, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=65, SP=8, ATK=12, DEF=11, INT=10, MIND=10, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=75, SP=9, ATK=13, DEF=12, INT=11, MIND=12, AGI=9, LUCK=0))
    stats.append(AttrDict(level=81, HP=80, SP=10, ATK=14, DEF=14, INT=11, MIND=14, AGI=10, LUCK=0))
    stats.append(AttrDict(level=86, HP=90, SP=11, ATK=15, DEF=16, INT=12, MIND=16, AGI=11, LUCK=0))
    stats.append(AttrDict(level=91, HP=95, SP=12, ATK=17, DEF=18, INT=13, MIND=18, AGI=11, LUCK=0))
    stats.append(AttrDict(level=96, HP=100, SP=13, ATK=20, DEF=20, INT=14, MIND=20, AGI=12, LUCK=0))


def extendLanteed():
    stats = MonsterTuning.LANTEED.LEVEL_STATS
    # AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=10, INT=7, MIND=10, AGI=7, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=10, INT=7, MIND=11, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=7, DEF=11, INT=8, MIND=10, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=45, SP=7, ATK=8, DEF=10, INT=8, MIND=12, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=50, SP=8, ATK=8, DEF=11, INT=9, MIND=11, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=60, SP=8, ATK=9, DEF=11, INT=10, MIND=12, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=70, SP=9, ATK=11, DEF=13, INT=11, MIND=13, AGI=9, LUCK=0))
    stats.append(AttrDict(level=81, HP=80, SP=10, ATK=13, DEF=15, INT=11, MIND=14, AGI=10, LUCK=0))
    stats.append(AttrDict(level=86, HP=90, SP=11, ATK=15, DEF=17, INT=12, MIND=16, AGI=11, LUCK=0))
    stats.append(AttrDict(level=91, HP=110, SP=12, ATK=17, DEF=20, INT=13, MIND=18, AGI=11, LUCK=0))
    stats.append(AttrDict(level=96, HP=125, SP=13, ATK=20, DEF=23, INT=14, MIND=20, AGI=12, LUCK=0))

    stats = MonsterTuning.PARAGON_LANTEED.LEVEL_STATS
    # AttrDict(level=46, HP=37, SP=6, ATK=9, DEF=12, INT=7, MIND=12, AGI=7, LUCK=0)
    stats.append(AttrDict(level=51, HP=37, SP=6, ATK=7, DEF=11, INT=7, MIND=11, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=43, SP=7, ATK=7, DEF=12, INT=8, MIND=12, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=50, SP=7, ATK=8, DEF=12, INT=8, MIND=12, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=70, SP=8, ATK=9, DEF=13, INT=9, MIND=13, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=90, SP=8, ATK=10, DEF=14, INT=10, MIND=14, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=110, SP=9, ATK=12, DEF=16, INT=11, MIND=13, AGI=9, LUCK=0))
    stats.append(AttrDict(level=81, HP=120, SP=10, ATK=14, DEF=16, INT=11, MIND=14, AGI=10, LUCK=0))
    stats.append(AttrDict(level=86, HP=130, SP=11, ATK=17, DEF=18, INT=12, MIND=16, AGI=11, LUCK=0))
    stats.append(AttrDict(level=91, HP=140, SP=12, ATK=20, DEF=20, INT=13, MIND=18, AGI=11, LUCK=0))
    stats.append(AttrDict(level=96, HP=150, SP=13, ATK=25, DEF=23, INT=14, MIND=20, AGI=12, LUCK=0))

    stats = MonsterTuning.LANTEED_SPROUT.LEVEL_STATS
    stats.append(AttrDict(level=41, HP=25, SP=0, ATK=0, DEF=11, INT=0, MIND=11, AGI=0, LUCK=0))
    stats.append(AttrDict(level=51, HP=30, SP=0, ATK=0, DEF=15, INT=0, MIND=14, AGI=0, LUCK=0))
    stats.append(AttrDict(level=61, HP=35, SP=0, ATK=0, DEF=18, INT=0, MIND=16, AGI=0, LUCK=0))
    stats.append(AttrDict(level=71, HP=40, SP=0, ATK=0, DEF=22, INT=0, MIND=18, AGI=0, LUCK=0))
    stats.append(AttrDict(level=81, HP=45, SP=0, ATK=0, DEF=25, INT=0, MIND=20, AGI=0, LUCK=0))
    stats.append(AttrDict(level=91, HP=50, SP=0, ATK=0, DEF=30, INT=0, MIND=22, AGI=0, LUCK=0))


def extendOilSlime():
    stats = MonsterTuning.OIL_SLIME.LEVEL_STATS
    # AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=10, INT=7, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=40, SP=6, ATK=7, DEF=10, INT=7, MIND=11, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=7, DEF=11, INT=8, MIND=10, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=45, SP=7, ATK=8, DEF=10, INT=8, MIND=12, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=45, SP=8, ATK=8, DEF=11, INT=9, MIND=11, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=50, SP=8, ATK=9, DEF=11, INT=10, MIND=12, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=50, SP=9, ATK=10, DEF=12, INT=11, MIND=13, AGI=9, LUCK=0))
    stats.append(AttrDict(level=81, HP=50, SP=10, ATK=11, DEF=13, INT=11, MIND=14, AGI=10, LUCK=0))
    stats.append(AttrDict(level=86, HP=55, SP=11, ATK=11, DEF=13, INT=12, MIND=14, AGI=11, LUCK=0))
    stats.append(AttrDict(level=91, HP=55, SP=12, ATK=10, DEF=13, INT=13, MIND=14, AGI=11, LUCK=0))
    stats.append(AttrDict(level=96, HP=60, SP=13, ATK=12, DEF=14, INT=14, MIND=15, AGI=12, LUCK=0))

    stats = MonsterTuning.PARAGON_OIL_SLIME.LEVEL_STATS
    # AttrDict(level=46, HP=22, SP=6, ATK=8, DEF=11, INT=8, MIND=11, AGI=7, LUCK=0)
    stats.append(AttrDict(level=51, HP=40, SP=6, ATK=7, DEF=10, INT=7, MIND=11, AGI=6, LUCK=0))
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=7, DEF=11, INT=8, MIND=10, AGI=7, LUCK=0))
    stats.append(AttrDict(level=61, HP=45, SP=7, ATK=8, DEF=10, INT=8, MIND=12, AGI=7, LUCK=0))
    stats.append(AttrDict(level=66, HP=45, SP=8, ATK=8, DEF=11, INT=9, MIND=11, AGI=8, LUCK=0))
    stats.append(AttrDict(level=71, HP=50, SP=8, ATK=9, DEF=11, INT=10, MIND=12, AGI=8, LUCK=0))
    stats.append(AttrDict(level=76, HP=50, SP=9, ATK=10, DEF=12, INT=11, MIND=13, AGI=9, LUCK=0))
    stats.append(AttrDict(level=81, HP=50, SP=10, ATK=11, DEF=13, INT=11, MIND=14, AGI=10, LUCK=0))
    stats.append(AttrDict(level=86, HP=55, SP=11, ATK=11, DEF=13, INT=12, MIND=14, AGI=11, LUCK=0))
    stats.append(AttrDict(level=91, HP=55, SP=12, ATK=10, DEF=13, INT=13, MIND=14, AGI=11, LUCK=0))
    stats.append(AttrDict(level=96, HP=60, SP=13, ATK=12, DEF=14, INT=14, MIND=15, AGI=12, LUCK=0))


def extendOrtomi():
    stats = MonsterTuning.ORTOMI.LEVEL_STATS
    # AttrDict(level=46, HP=30, SP=6, ATK=8, DEF=10, INT=7, MIND=10, AGI=9, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=8, DEF=10, INT=7, MIND=11, AGI=11, LUCK=0))
    stats.append(AttrDict(level=56, HP=25, SP=7, ATK=9, DEF=11, INT=8, MIND=10, AGI=11, LUCK=0))
    stats.append(AttrDict(level=61, HP=30, SP=7, ATK=10, DEF=10, INT=8, MIND=12, AGI=12, LUCK=0))
    stats.append(AttrDict(level=66, HP=35, SP=8, ATK=10, DEF=11, INT=9, MIND=11, AGI=13, LUCK=0))
    stats.append(AttrDict(level=71, HP=30, SP=8, ATK=11, DEF=11, INT=10, MIND=12, AGI=11, LUCK=0))
    stats.append(AttrDict(level=76, HP=35, SP=9, ATK=12, DEF=12, INT=11, MIND=13, AGI=12, LUCK=0))
    stats.append(AttrDict(level=81, HP=40, SP=10, ATK=13, DEF=13, INT=11, MIND=14, AGI=13, LUCK=0))
    stats.append(AttrDict(level=86, HP=35, SP=11, ATK=13, DEF=13, INT=12, MIND=14, AGI=13, LUCK=0))
    stats.append(AttrDict(level=91, HP=40, SP=12, ATK=14, DEF=13, INT=13, MIND=14, AGI=14, LUCK=0))
    stats.append(AttrDict(level=96, HP=45, SP=13, ATK=15, DEF=14, INT=14, MIND=15, AGI=15, LUCK=0))

    stats = MonsterTuning.PARAGON_ORTOMI.LEVEL_STATS
    # AttrDict(level=46, HP=25, SP=6, ATK=9, DEF=10, INT=7, MIND=11, AGI=10, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=9, DEF=10, INT=7, MIND=11, AGI=11, LUCK=0))
    stats.append(AttrDict(level=56, HP=35, SP=7, ATK=10, DEF=11, INT=8, MIND=10, AGI=11, LUCK=0))
    stats.append(AttrDict(level=61, HP=30, SP=7, ATK=11, DEF=10, INT=8, MIND=12, AGI=12, LUCK=0))
    stats.append(AttrDict(level=66, HP=35, SP=8, ATK=10, DEF=11, INT=9, MIND=11, AGI=13, LUCK=0))
    stats.append(AttrDict(level=71, HP=40, SP=8, ATK=11, DEF=11, INT=10, MIND=12, AGI=11, LUCK=0))
    stats.append(AttrDict(level=76, HP=35, SP=9, ATK=12, DEF=12, INT=11, MIND=13, AGI=12, LUCK=0))
    stats.append(AttrDict(level=81, HP=40, SP=10, ATK=13, DEF=13, INT=11, MIND=14, AGI=13, LUCK=0))
    stats.append(AttrDict(level=86, HP=45, SP=11, ATK=13, DEF=13, INT=12, MIND=14, AGI=13, LUCK=0))
    stats.append(AttrDict(level=91, HP=35, SP=12, ATK=14, DEF=13, INT=13, MIND=14, AGI=14, LUCK=0))
    stats.append(AttrDict(level=96, HP=40, SP=13, ATK=15, DEF=14, INT=14, MIND=15, AGI=15, LUCK=0))


def extendQuaridin():
    stats = MonsterTuning.QUARIDIN.LEVEL_STATS
    #AttrDict(level=46, HP=19, SP=6, ATK=7, DEF=10, INT=9, MIND=12, AGI=6, LUCK=0)

    stats.append(AttrDict(level=51, HP=23, SP=6, ATK=7, DEF=10, INT=9, MIND=11, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=24, SP=7, ATK=8, DEF=11, INT=10, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=25, SP=7, ATK=8, DEF=10, INT=10, MIND=12, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=20, SP=8, ATK=9, DEF=11, INT=11, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=25, SP=8, ATK=9, DEF=11, INT=12, MIND=12, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=27, SP=9, ATK=10, DEF=12, INT=12, MIND=13, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=28, SP=10, ATK=11, DEF=13, INT=11, MIND=14, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=29, SP=11, ATK=12, DEF=13, INT=12, MIND=14, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=30, SP=12, ATK=11, DEF=13, INT=13, MIND=14, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=35, SP=13, ATK=12, DEF=14, INT=14, MIND=15, AGI=9, LUCK=0));

    stats = MonsterTuning.PARAGON_QUARIDIN.LEVEL_STATS
    #AttrDict(level=46, HP=22, SP=6, ATK=10, DEF=14, INT=12, MIND=15, AGI=10, LUCK=0)

    stats.append(AttrDict(level=51, HP=23, SP=6, ATK=11, DEF=14, INT=11, MIND=15, AGI=10, LUCK=0));
    stats.append(AttrDict(level=56, HP=24, SP=7, ATK=11, DEF=15, INT=12, MIND=15, AGI=11, LUCK=0));
    stats.append(AttrDict(level=61, HP=25, SP=7, ATK=12, DEF=15, INT=12, MIND=16, AGI=12, LUCK=0));
    stats.append(AttrDict(level=66, HP=20, SP=8, ATK=13, DEF=14, INT=13, MIND=15, AGI=12, LUCK=0));
    stats.append(AttrDict(level=71, HP=25, SP=8, ATK=13, DEF=15, INT=13, MIND=15, AGI=13, LUCK=0));
    stats.append(AttrDict(level=76, HP=27, SP=9, ATK=14, DEF=16, INT=14, MIND=16, AGI=13, LUCK=0));
    stats.append(AttrDict(level=81, HP=28, SP=10, ATK=14, DEF=16, INT=15, MIND=17, AGI=14, LUCK=0));
    stats.append(AttrDict(level=86, HP=29, SP=11, ATK=15, DEF=17, INT=15, MIND=18, AGI=14, LUCK=0));
    stats.append(AttrDict(level=91, HP=30, SP=12, ATK=15, DEF=18, INT=14, MIND=19, AGI=15, LUCK=0));
    stats.append(AttrDict(level=96, HP=35, SP=13, ATK=15, DEF=20, INT=15, MIND=20, AGI=15, LUCK=0));

def extendIferos():
    stats = MonsterTuning.IFEROS.LEVEL_STATS
    #AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=11, INT=7, MIND=10, AGI=6, LUCK=0)

    stats.append(AttrDict(level=51, HP=35, SP=6, ATK=7, DEF=10, INT=7, MIND=11, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=8, DEF=11, INT=8, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=35, SP=7, ATK=8, DEF=10, INT=8, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=40, SP=8, ATK=9, DEF=11, INT=9, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=43, SP=8, ATK=9, DEF=11, INT=10, MIND=11, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=45, SP=9, ATK=10, DEF=12, INT=10, MIND=12, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=47, SP=10, ATK=11, DEF=13, INT=11, MIND=12, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=50, SP=11, ATK=12, DEF=13, INT=11, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=50, SP=12, ATK=11, DEF=13, INT=12, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=12, DEF=14, INT=12, MIND=14, AGI=9, LUCK=0));

def extendStegara():
    stats = MonsterTuning.STEGARA.LEVEL_STATS
    #AttrDict(level=46, HP=22, SP=6, ATK=8, DEF=10, INT=8, MIND=9, AGI=6, LUCK=0)

    stats.append(AttrDict(level=51, HP=25, SP=6, ATK=8, DEF=10, INT=8, MIND=9, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=27, SP=7, ATK=9, DEF=11, INT=9, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=30, SP=7, ATK=9, DEF=10, INT=9, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=33, SP=8, ATK=10, DEF=11, INT=10, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=35, SP=8, ATK=10, DEF=11, INT=11, MIND=11, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=35, SP=9, ATK=11, DEF=12, INT=11, MIND=12, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=37, SP=10, ATK=12, DEF=13, INT=12, MIND=12, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=40, SP=11, ATK=13, DEF=13, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=40, SP=12, ATK=14, DEF=13, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=45, SP=13, ATK=15, DEF=14, INT=14, MIND=14, AGI=9, LUCK=0));

    stats = MonsterTuning.PARAGON_STEGARA.LEVEL_STATS
    #AttrDict(level=46, HP=26, SP=6, ATK=16, DEF=14, INT=10, MIND=12, AGI=10, LUCK=0)

    stats.append(AttrDict(level=51, HP=27, SP=6, ATK=16, DEF=14, INT=8, MIND=12, AGI=10, LUCK=0));
    stats.append(AttrDict(level=56, HP=30, SP=7, ATK=17, DEF=15, INT=9, MIND=13, AGI=11, LUCK=0));
    stats.append(AttrDict(level=61, HP=33, SP=7, ATK=18, DEF=16, INT=9, MIND=14, AGI=12, LUCK=0));
    stats.append(AttrDict(level=66, HP=35, SP=8, ATK=20, DEF=16, INT=10, MIND=15, AGI=12, LUCK=0));
    stats.append(AttrDict(level=71, HP=37, SP=8, ATK=20, DEF=15, INT=11, MIND=15, AGI=13, LUCK=0));
    stats.append(AttrDict(level=76, HP=40, SP=9, ATK=20, DEF=15, INT=11, MIND=14, AGI=12, LUCK=0));
    stats.append(AttrDict(level=81, HP=43, SP=10, ATK=20, DEF=16, INT=12, MIND=15, AGI=14, LUCK=0));
    stats.append(AttrDict(level=86, HP=45, SP=11, ATK=22, DEF=17, INT=13, MIND=16, AGI=14, LUCK=0));
    stats.append(AttrDict(level=91, HP=47, SP=12, ATK=24, DEF=18, INT=13, MIND=16, AGI=15, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=16, DEF=20, INT=14, MIND=18, AGI=15, LUCK=0));

def extendMisc():
    stats = MonsterTuning.TARGET_DUMMY.LEVEL_STATS
    #AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=10, INT=7, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=40, SP=6, ATK=8, DEF=10, INT=8, MIND=9, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=9, DEF=11, INT=9, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=45, SP=7, ATK=9, DEF=10, INT=9, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=45, SP=8, ATK=10, DEF=11, INT=10, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=50, SP=8, ATK=10, DEF=11, INT=11, MIND=11, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=50, SP=9, ATK=11, DEF=12, INT=11, MIND=12, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=55, SP=10, ATK=12, DEF=13, INT=12, MIND=12, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=55, SP=11, ATK=13, DEF=13, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=60, SP=12, ATK=14, DEF=13, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=60, SP=13, ATK=15, DEF=14, INT=14, MIND=14, AGI=9, LUCK=0));

    stats = MonsterTuning.REBOUND_BALL.LEVEL_STATS
    #AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=10, INT=7, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=40, SP=6, ATK=8, DEF=10, INT=8, MIND=9, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=9, DEF=11, INT=9, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=45, SP=7, ATK=9, DEF=10, INT=9, MIND=10, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=45, SP=8, ATK=10, DEF=11, INT=10, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=50, SP=8, ATK=10, DEF=11, INT=11, MIND=11, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=50, SP=9, ATK=11, DEF=12, INT=11, MIND=12, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=55, SP=10, ATK=12, DEF=13, INT=12, MIND=12, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=55, SP=11, ATK=13, DEF=13, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=60, SP=12, ATK=14, DEF=13, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=60, SP=13, ATK=15, DEF=14, INT=14, MIND=14, AGI=9, LUCK=0));

def extendTelin():
    stats = MonsterTuning.TELIN.LEVEL_STATS
    #AttrDict(level=46, HP=34, SP=6, ATK=7, DEF=12, INT=8, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=37, SP=6, ATK=8, DEF=13, INT=8, MIND=11, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=9, DEF=13, INT=9, MIND=12, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=40, SP=7, ATK=9, DEF=14, INT=9, MIND=12, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=42, SP=8, ATK=10, DEF=14, INT=10, MIND=13, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=44, SP=8, ATK=10, DEF=15, INT=11, MIND=14, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=46, SP=9, ATK=11, DEF=15, INT=11, MIND=15, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=46, SP=10, ATK=12, DEF=16, INT=12, MIND=14, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=48, SP=11, ATK=13, DEF=16, INT=13, MIND=14, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=48, SP=12, ATK=14, DEF=17, INT=13, MIND=15, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=15, DEF=18, INT=14, MIND=15, AGI=9, LUCK=0));

def extendTenebrass():
    stats = MonsterTuning.TENEBRASS.LEVEL_STATS
    #AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=11, INT=7, MIND=10, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=35, SP=6, ATK=7, DEF=12, INT=8, MIND=11, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=8, DEF=12, INT=9, MIND=12, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=35, SP=7, ATK=8, DEF=13, INT=9, MIND=12, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=40, SP=8, ATK=9, DEF=14, INT=10, MIND=13, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=45, SP=8, ATK=10, DEF=14, INT=11, MIND=14, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=40, SP=9, ATK=10, DEF=15, INT=11, MIND=15, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=45, SP=10, ATK=11, DEF=15, INT=12, MIND=14, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=45, SP=11, ATK=12, DEF=16, INT=13, MIND=14, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=50, SP=12, ATK=13, DEF=16, INT=13, MIND=15, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=14, DEF=17, INT=14, MIND=15, AGI=9, LUCK=0));

def extendTorrend():
    stats = MonsterTuning.TORREND.LEVEL_STATS
    #AttrDict(level=46, HP=36, SP=6, ATK=10, DEF=8, INT=8, MIND=8, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=38, SP=6, ATK=10, DEF=8, INT=8, MIND=8, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=11, DEF=9, INT=9, MIND=9, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=38, SP=7, ATK=12, DEF=9, INT=9, MIND=9, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=40, SP=8, ATK=12, DEF=10, INT=10, MIND=10, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=42, SP=8, ATK=13, DEF=11, INT=11, MIND=11, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=44, SP=9, ATK=13, DEF=12, INT=11, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=46, SP=10, ATK=14, DEF=12, INT=12, MIND=12, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=46, SP=11, ATK=14, DEF=13, INT=13, MIND=12, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=48, SP=12, ATK=15, DEF=14, INT=13, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=15, DEF=15, INT=14, MIND=13, AGI=9, LUCK=0));

    stats = MonsterTuning.PARAGON_TORREND.LEVEL_STATS
    #AttrDict(level=46, HP=39, SP=6, ATK=14, DEF=8, INT=12, MIND=8, AGI=6, LUCK=0)

    stats.append(AttrDict(level=51, HP=38, SP=6, ATK=14, DEF=8, INT=12, MIND=8, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=40, SP=7, ATK=15, DEF=9, INT=13, MIND=9, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=38, SP=7, ATK=15, DEF=9, INT=13, MIND=9, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=40, SP=8, ATK=16, DEF=10, INT=14, MIND=10, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=42, SP=8, ATK=16, DEF=11, INT=14, MIND=11, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=44, SP=9, ATK=17, DEF=12, INT=15, MIND=11, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=46, SP=10, ATK=17, DEF=12, INT=15, MIND=12, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=46, SP=11, ATK=18, DEF=13, INT=16, MIND=12, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=48, SP=12, ATK=19, DEF=14, INT=17, MIND=13, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=20, DEF=15, INT=18, MIND=13, AGI=9, LUCK=0));

def extendZabis():
    stats = MonsterTuning.ZABIS.LEVEL_STATS
    #AttrDict(level=46, HP=28, SP=6, ATK=7, DEF=15, INT=6, MIND=12, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=15, INT=7, MIND=12, AGI=6, LUCK=0));
    stats.append(AttrDict(level=56, HP=32, SP=7, ATK=8, DEF=15, INT=8, MIND=13, AGI=7, LUCK=0));
    stats.append(AttrDict(level=61, HP=34, SP=7, ATK=9, DEF=16, INT=9, MIND=13, AGI=7, LUCK=0));
    stats.append(AttrDict(level=66, HP=36, SP=8, ATK=10, DEF=16, INT=10, MIND=14, AGI=8, LUCK=0));
    stats.append(AttrDict(level=71, HP=38, SP=8, ATK=11, DEF=17, INT=11, MIND=14, AGI=7, LUCK=0));
    stats.append(AttrDict(level=76, HP=40, SP=9, ATK=12, DEF=17, INT=11, MIND=15, AGI=8, LUCK=0));
    stats.append(AttrDict(level=81, HP=43, SP=10, ATK=13, DEF=18, INT=12, MIND=15, AGI=9, LUCK=0));
    stats.append(AttrDict(level=86, HP=46, SP=11, ATK=14, DEF=18, INT=13, MIND=16, AGI=10, LUCK=0));
    stats.append(AttrDict(level=91, HP=49, SP=12, ATK=15, DEF=19, INT=13, MIND=16, AGI=10, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=15, DEF=20, INT=14, MIND=17, AGI=9, LUCK=0));


    stats = MonsterTuning.PARAGON_ZABIS.LEVEL_STATS
    #AttrDict(level=46, HP=33, SP=6, ATK=12, DEF=20, INT=12, MIND=16, AGI=10, LUCK=0)
    stats.append(AttrDict(level=51, HP=36, SP=6, ATK=7, DEF=20, INT=7, MIND=16, AGI=10, LUCK=0));
    stats.append(AttrDict(level=56, HP=39, SP=7, ATK=8, DEF=21, INT=8, MIND=17, AGI=11, LUCK=0));
    stats.append(AttrDict(level=61, HP=42, SP=7, ATK=9, DEF=22, INT=9, MIND=18, AGI=12, LUCK=0));
    stats.append(AttrDict(level=66, HP=45, SP=8, ATK=10, DEF=23, INT=10, MIND=19, AGI=13, LUCK=0));
    stats.append(AttrDict(level=71, HP=48, SP=8, ATK=11, DEF=24, INT=11, MIND=20, AGI=14, LUCK=0));
    stats.append(AttrDict(level=76, HP=51, SP=9, ATK=12, DEF=25, INT=11, MIND=20, AGI=15, LUCK=0));
    stats.append(AttrDict(level=81, HP=54, SP=10, ATK=13, DEF=26, INT=12, MIND=20, AGI=16, LUCK=0));
    stats.append(AttrDict(level=86, HP=57, SP=11, ATK=14, DEF=27, INT=13, MIND=21, AGI=17, LUCK=0));
    stats.append(AttrDict(level=91, HP=60, SP=12, ATK=15, DEF=28, INT=13, MIND=22, AGI=18, LUCK=0));
    stats.append(AttrDict(level=96, HP=60, SP=13, ATK=15, DEF=30, INT=14, MIND=23, AGI=20, LUCK=0));

def extendVenfear():
    stats = MonsterTuning.VENFEAR.LEVEL_STATS
    #AttrDict(level=46, HP=28, SP=6, ATK=7, DEF=11, INT=7, MIND=10, AGI=10, LUCK=0)
    stats.append(AttrDict(level=51, HP=30, SP=6, ATK=7, DEF=11, INT=7, MIND=10, AGI=10, LUCK=0));
    stats.append(AttrDict(level=56, HP=32, SP=7, ATK=8, DEF=12, INT=8, MIND=11, AGI=11, LUCK=0));
    stats.append(AttrDict(level=61, HP=34, SP=7, ATK=9, DEF=13, INT=9, MIND=12, AGI=12, LUCK=0));
    stats.append(AttrDict(level=66, HP=36, SP=8, ATK=10, DEF=14, INT=10, MIND=13, AGI=13, LUCK=0));
    stats.append(AttrDict(level=71, HP=38, SP=8, ATK=11, DEF=15, INT=11, MIND=14, AGI=14, LUCK=0));
    stats.append(AttrDict(level=76, HP=40, SP=9, ATK=12, DEF=16, INT=11, MIND=15, AGI=15, LUCK=0));
    stats.append(AttrDict(level=81, HP=42, SP=10, ATK=13, DEF=17, INT=12, MIND=16, AGI=16, LUCK=0));
    stats.append(AttrDict(level=86, HP=44, SP=11, ATK=14, DEF=18, INT=13, MIND=17, AGI=17, LUCK=0));
    stats.append(AttrDict(level=91, HP=47, SP=12, ATK=15, DEF=19, INT=13, MIND=18, AGI=18, LUCK=0));
    stats.append(AttrDict(level=96, HP=50, SP=13, ATK=15, DEF=20, INT=14, MIND=20, AGI=20, LUCK=0));

def extendBosses():
    extendBaritus()
    extendDormian()
    extendGildor()
    extendSano()

def extendBaritus():
    stats = MonsterTuning.BARITUS.LEVEL_STATS
    #AttrDict(level=41, HP=500, SP=10, ATK=25, DEF=24, INT=23, MIND=24, AGI=23, LUCK=0)
    stats.append(AttrDict(level=51, HP=300, SP=6, ATK=28, DEF=26, INT=25, MIND=26, AGI=26, LUCK=0));
    stats.append(AttrDict(level=61, HP=200, SP=7, ATK=26, DEF=30, INT=30, MIND=30, AGI=30, LUCK=0));
    stats.append(AttrDict(level=71, HP=400, SP=7, ATK=33, DEF=34, INT=35, MIND=34, AGI=35, LUCK=0));
    stats.append(AttrDict(level=81, HP=300, SP=8, ATK=41, DEF=38, INT=42, MIND=38, AGI=40, LUCK=0));
    stats.append(AttrDict(level=91, HP=600, SP=8, ATK=50, DEF=42, INT=54, MIND=42, AGI=45, LUCK=0));

    stats = MonsterTuning.BARITUS_ALTAR.LEVEL_STATS
    #AttrDict(level=41, HP=200, SP=0, ATK=25, DEF=24, INT=20, MIND=22, AGI=21, LUCK=0)
    stats.append(AttrDict(level=51, HP=400, SP=0, ATK=30, DEF=28, INT=25, MIND=26, AGI=0, LUCK=0));
    stats.append(AttrDict(level=61, HP=0, SP=0, ATK=0, DEF=24, INT=0, MIND=21, AGI=0, LUCK=0));
    stats.append(AttrDict(level=71, HP=400, SP=0, ATK=35, DEF=0, INT=30, MIND=0, AGI=0, LUCK=0));
    stats.append(AttrDict(level=81, HP=0, SP=0, ATK=0, DEF=32, INT=0, MIND=27, AGI=0, LUCK=0));
    stats.append(AttrDict(level=91, HP=800, SP=0, ATK=40, DEF=36, INT=35, MIND=30, AGI=0, LUCK=0));

def extendDormian():
    stats = MonsterTuning.DORMIAN.LEVEL_STATS
    #AttrDict(level=41, HP=350, SP=5, ATK=15, DEF=13, INT=20, MIND=16, AGI=13, LUCK=0)
    stats.append(AttrDict(level=51, HP=450, SP=6, ATK=20, DEF=16, INT=25, MIND=18, AGI=16, LUCK=0));
    stats.append(AttrDict(level=61, HP=600, SP=7, ATK=26, DEF=20, INT=30, MIND=24, AGI=20, LUCK=0));
    stats.append(AttrDict(level=71, HP=800, SP=7, ATK=33, DEF=25, INT=35, MIND=31, AGI=25, LUCK=0));
    stats.append(AttrDict(level=81, HP=1000, SP=8, ATK=41, DEF=31, INT=42, MIND=39, AGI=31, LUCK=0));
    stats.append(AttrDict(level=91, HP=1250, SP=8, ATK=50, DEF=38, INT=54, MIND=48, AGI=38, LUCK=0));

    stats = MonsterTuning.SPAWN_SPHERE.LEVEL_STATS
    #AttrDict(level=41, HP=350, SP=5, ATK=15, DEF=13, INT=20, MIND=16, AGI=13, LUCK=0)
    stats.append(AttrDict(level=51, HP=100, SP=0, ATK=0, DEF=20, INT=0, MIND=18, AGI=0, LUCK=0));
    stats.append(AttrDict(level=61, HP=130, SP=0, ATK=0, DEF=24, INT=0, MIND=21, AGI=0, LUCK=0));
    stats.append(AttrDict(level=71, HP=170, SP=0, ATK=0, DEF=28, INT=0, MIND=24, AGI=0, LUCK=0));
    stats.append(AttrDict(level=81, HP=220, SP=0, ATK=0, DEF=32, INT=0, MIND=27, AGI=0, LUCK=0));
    stats.append(AttrDict(level=91, HP=300, SP=0, ATK=0, DEF=36, INT=0, MIND=30, AGI=0, LUCK=0));

def extendGildor():
    stats = MonsterTuning.GILDOR.LEVEL_STATS
    #AttrDict(level=41, HP=90, SP=8, ATK=18, DEF=20, INT=16, MIND=20, AGI=6, LUCK=0)
    stats.append(AttrDict(level=51, HP=120, SP=6, ATK=22, DEF=25, INT=20, MIND=25, AGI=18, LUCK=0));
    stats.append(AttrDict(level=61, HP=240, SP=7, ATK=25, DEF=30, INT=24, MIND=30, AGI=22, LUCK=0));
    stats.append(AttrDict(level=71, HP=400, SP=7, ATK=28, DEF=35, INT=28, MIND=35, AGI=27, LUCK=0));
    stats.append(AttrDict(level=81, HP=600, SP=8, ATK=31, DEF=40, INT=32, MIND=40, AGI=33, LUCK=0));
    stats.append(AttrDict(level=91, HP=900, SP=8, ATK=35, DEF=50, INT=46, MIND=50, AGI=40, LUCK=0));

    stats = MonsterTuning.GILDOR_PILLAR.LEVEL_STATS
    #AttrDict(level=41, HP=70, SP=0, ATK=0, DEF=16, INT=0, MIND=15, AGI=0, LUCK=0)
    stats.append(AttrDict(level=51, HP=100, SP=0, ATK=0, DEF=20, INT=0, MIND=18, AGI=0, LUCK=0));
    stats.append(AttrDict(level=61, HP=130, SP=0, ATK=0, DEF=24, INT=0, MIND=21, AGI=0, LUCK=0));
    stats.append(AttrDict(level=71, HP=170, SP=0, ATK=0, DEF=28, INT=0, MIND=24, AGI=0, LUCK=0));
    stats.append(AttrDict(level=81, HP=220, SP=0, ATK=0, DEF=32, INT=0, MIND=27, AGI=0, LUCK=0));
    stats.append(AttrDict(level=91, HP=300, SP=0, ATK=0, DEF=36, INT=0, MIND=30, AGI=0, LUCK=0));

def extendSano():
    stats = MonsterTuning.SANO.LEVEL_STATS
    #AttrDict(level=41, HP=320, SP=6, ATK=20, DEF=18, INT=22, MIND=21, AGI=15, LUCK=0)
    stats.append(AttrDict(level=51, HP=420, SP=6, ATK=30, DEF=26, INT=30, MIND=25, AGI=18, LUCK=0));
    stats.append(AttrDict(level=61, HP=540, SP=7, ATK=40, DEF=32, INT=42, MIND=30, AGI=22, LUCK=0));
    stats.append(AttrDict(level=71, HP=660, SP=7, ATK=50, DEF=40, INT=54, MIND=35, AGI=27, LUCK=0));
    stats.append(AttrDict(level=81, HP=780, SP=8, ATK=60, DEF=50, INT=66, MIND=40, AGI=33, LUCK=0));
    stats.append(AttrDict(level=91, HP=1000, SP=8, ATK=70, DEF=65, INT=80, MIND=50, AGI=40, LUCK=0));

def extendSpawners():
    new_stats = [
        AttrDict(level=51, HP=25, DEF=12, MIND=11),
        AttrDict(level=56, HP=30, DEF=13, MIND=12),
        AttrDict(level=61, HP=30, DEF=14, MIND=13),
        AttrDict(level=66, HP=35, DEF=15, MIND=14),
        AttrDict(level=71, HP=35, DEF=15, MIND=15),
        AttrDict(level=76, HP=40, DEF=16, MIND=16),
        AttrDict(level=81, HP=45, DEF=17, MIND=17),
        AttrDict(level=86, HP=50, DEF=18, MIND=18),
        AttrDict(level=91, HP=55, DEF=19, MIND=19),
        AttrDict(level=96, HP=60, DEF=20, MIND=20)
    ]

    SpawnerTuning.AEGNITE_SPAWNER.LEVEL_STATS = SpawnerTuning.AEGNITE_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.AMONE_SPAWNER.LEVEL_STATS = SpawnerTuning.AMONE_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.CENFEN_SPAWNER.LEVEL_STATS = SpawnerTuning.CENFEN_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.CORTESS_SPAWNER.LEVEL_STATS = SpawnerTuning.CORTESS_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.ELTRET_SPAWNER.LEVEL_STATS = SpawnerTuning.ELTRET_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.GLOW_BAT_SPAWNER.LEVEL_STATS = SpawnerTuning.GLOW_BAT_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.HARVESTER_SPAWNER.LEVEL_STATS = SpawnerTuning.HARVESTER_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.IFEROS_SPAWNER.LEVEL_STATS = SpawnerTuning.IFEROS_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.LANTEED_SPAWNER.LEVEL_STATS = SpawnerTuning.LANTEED_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.OIL_SLIME_SPAWNER.LEVEL_STATS = SpawnerTuning.OIL_SLIME_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.ORTOMI_SPAWNER.LEVEL_STATS = SpawnerTuning.ORTOMI_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.QUARIDIN_SPAWNER.LEVEL_STATS = SpawnerTuning.QUARIDIN_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.STEGARA_SPAWNER.LEVEL_STATS = SpawnerTuning.STEGARA_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.TELIN_SPAWNER.LEVEL_STATS = SpawnerTuning.TELIN_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.TORREND_SPAWNER.LEVEL_STATS = SpawnerTuning.TORREND_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.TENEBRASS_SPAWNER.LEVEL_STATS = SpawnerTuning.TENEBRASS_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.VENFEAR_SPAWNER.LEVEL_STATS = SpawnerTuning.VENFEAR_SPAWNER.LEVEL_STATS + new_stats
    SpawnerTuning.ZABIS_SPAWNER.LEVEL_STATS = SpawnerTuning.ZABIS_SPAWNER.LEVEL_STATS + new_stats
