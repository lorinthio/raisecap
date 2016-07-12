from core.effect.base import EffectBase
from core.monster import MonsterState
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege.util import Vector


class Snare(EffectBase):
    TUNING = EffectTuning.SNARE

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Snare, self).__init__(owner, duration, isRefresh)
        self.owner = owner
        if owner.has('physics'):
            if owner.has('monster'):
                monster = owner.monster.core
                self.originalRoamSpeed = monster.roamSpeed
                self.originalHostileSpeed = monster.hostileSpeed
                monster.roamSpeed = Vector()
                monster.hostileSpeed = Vector()
                if monster.state is MonsterState.Roam or monster.state is MonsterState.Hostile:
                    monster.changeState(MonsterState.Idle)

    def onRemove(self, owner):
        if owner.has('physics') and owner.has('monster'):
            owner.monster.core.roamSpeed = self.originalRoamSpeed
            owner.monster.core.hostileSpeed = self.originalHostileSpeed

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Snare.TUNING.NAME, Snare)
