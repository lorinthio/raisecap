from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege.util import seconds, Timer, Vector


class Paralyze(EffectBase):
    TUNING = EffectTuning.PARALYZE

    def __init__(self, owner, level, duration, source, isRefresh):
        self.nextParalysis = Timer(self.TUNING.NEXT_PARALYSIS.getRandom())
        self.paralyzeTimer = Timer()
        self.owner = owner
        self.owner.physics.onTimeStep.listen(self.handleParalyzeTimer)

        super(Paralyze, self).__init__(owner, duration, isRefresh)

    def handleParalyzeTimer(self, physics, frameTime):
        self.nextParalysis.update(frameTime)
        if self.nextParalysis.expired():
            self.paralyze()
            return True

    def paralyze(self):
        if self.owner.combat.isAlive.get():
            self.owner.animation.play("idle")
            if self.owner.has('playerState'):
                self.owner.playerState.canAttack.set(False)
                self.owner.playerState.canCast.set(False)
                self.owner.playerState.canMove.set(False)
            if self.owner.has('physics'):
                if self.owner.has('monster'):
                    self.originalSpeed = self.owner.monster.core.speed
                    self.originalHostileSpeed = self.owner.monster.core.hostileSpeed
                    self.owner.monster.core.speed = Vector(0, 0)
                    self.owner.monster.core.hostileSpeed = Vector(0, 0)
                velocity = self.owner.physics.getVelocity()
                velocity.x = 0
                self.owner.physics.setVelocity(velocity)
                self.paralyzeTimer.reset(seconds(1))
                self.owner.physics.onTimeStep.listen(self.handleParalyze)

    def handleParalyze(self, physics, frameTime):
        self.paralyzeTimer.update(frameTime)
        if self.paralyzeTimer.expired():
            self.removeParalysis()
            self.nextParalysis.reset(self.TUNING.NEXT_PARALYSIS.getRandom())
            physics.onTimeStep.listen(self.handleParalyzeTimer)
            return True

    def removeParalysis(self):
        if self.owner.has('playerState'):
            self.owner.playerState.canAttack.set(True)
            self.owner.playerState.canCast.set(True)
            self.owner.playerState.canMove.set(True)
        if self.owner.has('physics'):
            if self.owner.has('monster'):
                self.owner.monster.core.speed = self.originalSpeed
                self.owner.monster.core.hostileSpeed = self.originalHostileSpeed
            self.owner.physics.onTimeStep.remove(self.handleParalyze)
            self.owner.physics.onTimeStep.remove(self.handleParalyzeTimer)

    def onRemove(self, owner):
        self.removeParalysis()

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Paralyze.TUNING.NAME, Paralyze)
