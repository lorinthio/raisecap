from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game


class Invincible(EffectBase):
    TUNING = EffectTuning.INVINCIBLE

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Invincible, self).__init__(owner, duration, isRefresh)
        owner.combat.setInvincible(True)

    def onRemove(self, owner):
        owner.combat.setInvincible(False)

    @staticmethod
    def register():
        game.effects.register(Invincible.TUNING.NAME, Invincible)
