from core.effect.base import EffectBase
from core.helper import chance
from core.tuning.skill import SkillTuning
from raisecap.tuning.effect import EffectTuning

from siege import game, Locale


class Precision(EffectBase):
    TUNING = EffectTuning.PRECISION

    @property
    def description(self):
        return Locale.getEscaped(Precision.TUNING.DESC).format(chance=Locale.getEscaped(self.chance))

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Precision, self).__init__(owner, duration, isRefresh)
        self.chance = SkillTuning.PRECISION.CHANCES[level - 1]
        if owner.isPlayer():
            owner.event['tool_power'].listen(self.handleToolPower)

    def handleToolPower(self, player, results, tool, power):
        if chance(self.chance):
            results.power = 9999

    def onRemove(self, owner):
        if owner.isPlayer():
            owner.event['tool_power'].remove(self.handleToolPower)

    @staticmethod
    def register():
        game.effects.register(Precision.TUNING.NAME, Precision)
