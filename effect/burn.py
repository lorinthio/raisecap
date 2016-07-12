from core.combat import applyDamage
from core.effect.base import EffectBase
from core.helper import getEntityCenter
from raisecap.tuning.effect import EffectTuning
from core.util import DamageSource

from siege import game
from siege.graphic import Color
from siege.network import NetworkManager
from siege.util import Random, RangeFloat, RangeUint, seconds, Vector


class Burn(EffectBase):
    TUNING = EffectTuning.BURN

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Burn, self).__init__(owner, duration, isRefresh)
        self.amount = owner.stats.HP.getMax() * (Burn.TUNING.PERCENTAGE_PER_TICK / 100.0) * level
        self.removeExistingDebuffs(owner)

    def removeExistingDebuffs(self, owner):
        for effect in[EffectTuning.BREATHLESS.NAME, EffectTuning.FROSTBITE.NAME, EffectTuning.WEIGHTED.NAME]:
            owner.effects.remove(effect)

    def update(self, frameTime, owner):
        if game.isOnTick() and NetworkManager.isHost():
            self.emitEmbers(owner)
            applyDamage(owner, self.amount, origin=None, knockback=None, damageSource=DamageSource.Burning)
            if owner.has("combat"):
                # Reset combat time so the player doesn't get out of combat health regen
                owner.combat.timeSinceCombat = 0
        return True

    def isPositive(self):
        return False

    def emitEmbers(self, entity):
        position = getEntityCenter(entity)
        position.x -= 4
        position.y -= 10
        realm = entity.realm
        emitter = game.particles.create(realm.uid, realm.loopWidth, position, amount=Random.get(2, 6), texturePath="mods/core/talent/syle/fire_particle.png", hasPhysics=True)
        emitter.x.setRange(RangeFloat(-3, 4))
        emitter.y.setRange(RangeFloat(-1, 0))
        emitter.alpha.set(255, 0, duration=500).delay(RangeUint(seconds(2), seconds(3)))
        emitter.scale.setList([Vector(1, 1), Vector(2, 2)], [Vector(0.5, 0.5), Vector(1, 1)])
        emitter.rotation.setRange(0, RangeFloat(-90, 90))
        emitter.gravity = Vector(0.0, 0.08)
        emitter.friction = Vector(0.1, 0.0)
        emitter.restitution = Vector(0.2, 0.4)
        emitter.addLightSource(decay=3, color=Color(220, 120, 40))

    @staticmethod
    def register():
        game.effects.register(Burn.TUNING.NAME, Burn)
