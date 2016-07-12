from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game


class Invigorated(EffectBase):
    TUNING = EffectTuning.INVIGORATED

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Invigorated, self).__init__(owner, duration, isRefresh)
        self.statUid = owner.stats.SPRegen.mod(self.TUNING.AMOUNT)

    def onRemove(self, owner):
        owner.stats.SPRegen.unmod(self.statUid)

    @staticmethod
    def register():
        game.effects.register(Invigorated.TUNING.NAME, Invigorated)
