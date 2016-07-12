from core.effect.base import EffectBase
from core.tuning.skill import SkillTuning
from raisecap.tuning.effect import EffectTuning
from siege import game


class Regen(EffectBase):
    TUNING = EffectTuning.REGEN

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Regen, self).__init__(owner, duration, isRefresh)
        self.adjustment = owner.stats.HP.getMax() * SkillTuning.REGENERATE.HEALTH_PERCENTAGES[level - 1] / 100.0
        self.statUid = owner.stats.HPRegen.mod(self.adjustment)

    def onRemove(self, owner):
        owner.stats.HPRegen.unmod(self.statUid)

    @staticmethod
    def register():
        game.effects.register(Regen.TUNING.NAME, Regen)
