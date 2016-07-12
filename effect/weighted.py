from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege.util import Vector


class Weighted(EffectBase):
    TUNING = EffectTuning.WEIGHTED

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Weighted, self).__init__(owner, duration, isRefresh)

        self.amount = (100 - self.TUNING.AMOUNT) / 100.00
        if owner.has('monster'):
            self.roamSpeed = owner.monster.core.roamSpeed
            self.hostileSpeed = owner.monster.core.hostileSpeed

            owner.monster.core.roamSpeed = Vector(self.roamSpeed.x * self.amount, self.roamSpeed.y * self.amount)
            owner.monster.core.hostileSpeed = Vector(self.hostileSpeed.x * self.amount, self.hostileSpeed.y * self.amount)

        self.removeExistingDebuffs(owner)

    def removeExistingDebuffs(self, owner):
        for effect in[EffectTuning.BURN.NAME, EffectTuning.BREATHLESS.NAME, EffectTuning.FROSTBITE.NAME]:
            owner.effects.remove(effect)

    def onRemove(self, owner):
        if owner.has('monster'):
            owner.monster.core.roamSpeed = self.roamSpeed
            owner.monster.core.hostileSpeed = self.hostileSpeed

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Weighted.TUNING.NAME, Weighted)
