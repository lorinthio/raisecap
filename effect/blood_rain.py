from core.combat import applyDamage
from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from core.util import DamageSource

from siege import game
from siege.network import NetworkManager


class BloodRain(EffectBase):
    TUNING = EffectTuning.BLOOD_RAIN

    def __init__(self, owner, level, duration, source, isRefresh):
        super(BloodRain, self).__init__(owner, duration, isRefresh)
        self.amount = owner.stats.HP.getMax() / 25

    def update(self, frameTime, owner):
        if NetworkManager.isHost() and game.isOnTick() and owner.combat.isAlive.get():
            applyDamage(owner, self.amount, origin=None, knockback=None, damageSource=DamageSource.BloodRain)
            # Reset combat time so the player doesn't get out of combat health regen
            owner.combat.timeSinceCombat = 0
        return True

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(BloodRain.TUNING.NAME, BloodRain)
