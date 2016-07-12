from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege.util import Vector


class Stun(EffectBase):
    TUNING = EffectTuning.STUN

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Stun, self).__init__(owner, duration, isRefresh)
        owner.animation.play("idle")
        if owner.has('physics'):
            if owner.has('monster'):
                self.originalSpeed = owner.monster.core.speed
                self.originalHostileSpeed = owner.monster.core.hostileSpeed
                owner.monster.core.speed = Vector(0, 0)
                owner.monster.core.hostileSpeed = Vector(0, 0)
            velocity = owner.physics.getVelocity()
            velocity.x = 0
            owner.physics.setVelocity(velocity)
        if owner.has('playerState'):
            owner.playerState.canAttack.set(False)
            owner.playerState.canCast.set(False)
            owner.playerState.canMove.set(False)

    def onRemove(self, owner):
        if owner.has('physics') and owner.has('monster'):
            owner.monster.core.speed = self.originalSpeed
            owner.monster.core.hostileSpeed = self.originalHostileSpeed
        if owner.has('playerState'):
            owner.playerState.canAttack.set(True)
            owner.playerState.canCast.set(True)
            owner.playerState.canMove.set(True)

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Stun.TUNING.NAME, Stun)
