from core.talent import addSkill, PassiveSkill, getTuningData
from raisecap.tuning.skill import SkillTuning
from functools import partial

from siege.log import Log


def modifyArmsTalent(talent):
    pass


def modifySyleTalent(talent):
    pass


def modifyGatherTalent(talent):
    pass


def modifyExploreTalent(talent):
    addSkill(talent, FeatherFalling)
    Log.info('Modified the explore talent!')


def modifyCraftTalent(talent):
    pass


class FeatherFalling(PassiveSkill):
    TUNING = SkillTuning.FEATHER_FALLING
    modifiers = ['FALL_REDUCTION']

    def onActivate(self, level, player):
        player.entity.event["descent_damage"].listen(partial(FeatherFalling.onFall, level))

    def onDeactivate(self, level, player):
        player.entity.event["descent_damage"].remove(partial(FeatherFalling.onFall, level))

    @staticmethod
    def onFall(level, player, results, damage):
        results.damage -= int(results.damage * (getTuningData(FeatherFalling.TUNING, level, 'FALL_REDUCTION') / 100.00))
