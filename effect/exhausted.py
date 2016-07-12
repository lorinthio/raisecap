from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game
from siege.network import NetworkManager


class Exhausted(EffectBase):
    TUNING = EffectTuning.EXHAUSTED

    def __init__(self, owner, level, duration, source, isRefresh):
        if NetworkManager.isHost():
            self.owner = owner
            owner.combat.canRecover.set(False)
            game.timer.add(500, self.enableRecovery, isExitJob=True)

    def enableRecovery(self):
        self.owner.combat.canRecover.set(True)

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Exhausted.TUNING.NAME, Exhausted)
