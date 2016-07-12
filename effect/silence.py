from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game


class Silence(EffectBase):
    TUNING = EffectTuning.SILENCE

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Silence, self).__init__(owner, duration, isRefresh)
        if owner.has('playerState'):
            owner.playerState.canCast.set(False)

    def onRemove(self, owner):
        if owner.has('playerState'):
            owner.playerState.canCast.set(True)

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Silence.TUNING.NAME, Silence)
