from core.tuning.monster import MonsterTuning
from core.tuning.player import PlayerTuning
from raisecap.tuning.effect import EffectTuning
import raisecap.effect

from siege import game
from siege.log import Log

import raisecap.tuning.modified as modified
import raisecap.tuning.extendedMobs as extendedMobs
from raisecap.tuning.skill import SkillTuning


def updateLevels():
    DESIRED_MAX_LEVEL = 100
    # Raise monster max level to our new cap
    MonsterTuning.MAX_LEVEL = DESIRED_MAX_LEVEL
    extendedMobs.extendMobs()
    SkillTuning()
    EffectTuning()

    raisecap.effect.register()


def register():
    game.onUnregistration.listen(systemUnregistration)
    game.events['create_talent'].listen(tweakTalents)
    tweakLevels()
    updateLevels()


def systemUnregistration():
    game.onUnregistration.remove(systemUnregistration)
    game.events['create_talent'].remove(tweakTalents)
    game.events['world_loaded'].remove(tweakLevels)


def tweakTalents(talent):
    talent.levels = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950] + [1000] * 30 + [1200] * 20 + [1400] * 10 + [1600] * 10 + [1800] * 10 + [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3700, 4000]
    if talent.name == 'explore':
        modified.modifyExploreTalent(talent)


def tweakLevels():
    # Raise player max level
    PlayerTuning.LEVELS_EXPERIENCE_REQUIRED = [400, 450, 500, 550, 600, 650, 700, 800, 900] + [1000] * 20 + [1500] * 10 + [2000] * 10 + [2200] * 20 + [2400] * 15 + [2600] * 5 + [2800] * 5 + [3000, 3400, 3800, 4400, 5000]
    Log.info(str(PlayerTuning.LEVELS_EXPERIENCE_REQUIRED))
