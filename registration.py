from core.system.conflict import ConflictRegion
from core.tuning.monster import MonsterTuning
from core.tuning.player import PlayerTuning as pTuning
from raisecap.tuning.effect import EffectTuning
import raisecap.effect

from siege import game

import raisecap.tuning.modified as modified
import raisecap.tuning.extendedMobs as extendedMobs
from raisecap.tuning.player import PlayerTuning
from raisecap.tuning.skill import SkillTuning


def updateLevels():
    DESIRED_MAX_LEVEL = 100
    # Raise player max level
    pTuning.LEVEL_EXPERIENCE_REQUIRED = PlayerTuning.LEVEL_EXPERIENCE_REQUIRED
    # Raise monster max level to our new cap
    MonsterTuning.MAX_LEVEL = DESIRED_MAX_LEVEL
    # Raise the level cap of the conflict regions from 50, to the new cap
    ConflictRegion.HOSTILITY_CAP = DESIRED_MAX_LEVEL
    extendedMobs.extendMobs()
    SkillTuning()
    EffectTuning()

    raisecap.effect.register()


def register():
    game.onUnregistration.listen(systemUnregistration)
    game.events['create_talent'].listen(tweakTalents)
    updateLevels()


def systemUnregistration():
    game.onUnregistration.remove(systemUnregistration)
    game.events['create_talent'].remove(tweakTalents)


def tweakTalents(talent):
    talent.levels = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950] + [1000] * 30 + [1200] * 20 + [1400] * 10 + [1600] * 10 + [1800] * 10 + [2000, 2200, 2400, 2700, 3000, 3500, 4000, 4500, 5000, 5000]
    if talent.name == 'explore':
        modified.modifyExploreTalent(talent)
