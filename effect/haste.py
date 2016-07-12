from core.effect.base import EffectBase
from core.tuning.skill import SkillTuning
from raisecap.tuning.effect import EffectTuning
from siege import game


class Haste(EffectBase):
    TUNING = EffectTuning.HASTE

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Haste, self).__init__(owner, duration, isRefresh)
        self.adjustment = SkillTuning.HASTE.ATTACK_SPEEDS[level - 1]
        self.statUid = owner.stats.SPD.mod(self.adjustment)

    def onRemove(self, owner):
        owner.stats.SPD.unmod(self.statUid)

    @staticmethod
    def register():
        game.effects.register(Haste.TUNING.NAME, Haste)
