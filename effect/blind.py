from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game


class Blind(EffectBase):
    TUNING = EffectTuning.BLIND

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Blind, self).__init__(owner, duration, isRefresh)
        self.statUid = owner.stats.ACC.mod(-Blind.TUNING.AMOUNT)

    def onRemove(self, owner):
        owner.stats.ACC.unmod(self.statUid)

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Blind.TUNING.NAME, Blind)
