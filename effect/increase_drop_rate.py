from core.effect.base import EffectBase
from core.talent import getTuningData
from raisecap.tuning.effect import EffectTuning
from raisecap.tuning.skill import SkillTuning

from siege import game, Locale


class IncreaseDropRate(EffectBase):
    TUNING = EffectTuning.INCREASE_DROP_RATE

    @property
    def description(self):
        amount = getTuningData(SkillTuning.INCREASE_DROP_RATE, self.level, 'AMOUNT')
        return Locale.getEscaped(IncreaseDropRate.TUNING.DESC).format(amount=amount)

    def __init__(self, owner, level, duration, source, isRefresh):
        super(IncreaseDropRate, self).__init__(owner, duration, isRefresh)
        self.level = level
        self.removeExistingDebuff(owner)

    def removeExistingDebuff(self, owner):
        owner.effects.remove(EffectTuning.INCREASE_DROP_RATE.NAME)

    def onRemove(self, owner):
        pass

    @staticmethod
    def register():
        game.effects.register(IncreaseDropRate.TUNING.NAME, IncreaseDropRate)
