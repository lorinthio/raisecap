from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game, Locale


class Frostbite(EffectBase):
    TUNING = EffectTuning.FROSTBITE

    @property
    def description(self):
        return Locale.getEscaped(self.TUNING.DESC).format(amount=self.TUNING.AMOUNT)

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Frostbite, self).__init__(owner, duration, isRefresh)

        self.defenseAdjustment = owner.stats.DEF.get() * self.TUNING.AMOUNT / 100
        self.statUid = owner.stats.DEF.mod(-self.defenseAdjustment)

        self.removeExistingDebuffs(owner)

    def removeExistingDebuffs(self, owner):
        for effect in[EffectTuning.BURN.NAME, EffectTuning.BREATHLESS.NAME, EffectTuning.WEIGHTED.NAME]:
            owner.effects.remove(effect)

    def onRemove(self, owner):
        owner.stats.DEF.unmod(self.statUid)

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Frostbite.TUNING.NAME, Frostbite)
