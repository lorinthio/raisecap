from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game


class Breathless(EffectBase):
    TUNING = EffectTuning.BREATHLESS

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Breathless, self).__init__(owner, duration, isRefresh)

        self.amount = 1.00 + self.TUNING.AMOUNT / 100.00
        if owner.has('monster'):
            self.cooldowns = []
            for action in owner.monster.core.actions:
                try:
                    self.cooldowns.append(action.cooldownTime)
                    action.cooldownTime = int(action.cooldownTime * self.amount)
                except:
                    self.cooldowns.append("pass")

        self.removeExistingDebuffs(owner)

    def removeExistingDebuffs(self, owner):
        for effect in[EffectTuning.BURN.NAME, EffectTuning.FROSTBITE.NAME, EffectTuning.WEIGHTED.NAME]:
            owner.effects.remove(effect)

    def onRemove(self, owner):
        if owner.has('monster'):
            for i in range(len(self.cooldowns)):
                if not self.cooldowns[i] == "pass":
                    owner.monster.core.actions[i].cooldownTime = self.cooldowns[i]

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Breathless.TUNING.NAME, Breathless)
