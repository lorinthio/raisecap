from core.combat import applyDamage
from core.effect.base import EffectBase
from core.talent import emitSupportParticles
from raisecap.tuning.effect import EffectTuning
from core.util import DamageSource

from siege import game
from siege.network import NetworkManager
from siege.util import PixelRect


class ChaosBurn(EffectBase):
    TUNING = EffectTuning.CHAOS_BURN
    PARTICLE_COORDS = [
        PixelRect(0, 0, 7, 7),
        PixelRect(7, 1, 5, 5),
        PixelRect(8, 2, 3, 3)
    ]

    def __init__(self, owner, level, duration, source, isRefresh):
        super(ChaosBurn, self).__init__(owner, duration, isRefresh)
        self.amount = owner.stats.HP.getMax() * (ChaosBurn.TUNING.PERCENTAGE_PER_TICK / 100.0) * level

    def update(self, frameTime, owner):
        if game.isOnTick() and NetworkManager.isHost():
            emitSupportParticles(owner.realm, owner, 'mods/core/monster/baritus/altar/chaos_particles.png', ChaosBurn.PARTICLE_COORDS)
            applyDamage(owner, self.amount, origin=None, knockback=None, damageSource=DamageSource.Burning)
            if owner.has("combat"):
                # Reset combat time so the player doesn't get out of combat health regen
                owner.combat.timeSinceCombat = 0
        return True

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(ChaosBurn.TUNING.NAME, ChaosBurn)
