from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game


class Reraise(EffectBase):
    TUNING = EffectTuning.RERAISE

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Reraise, self).__init__(owner, duration, isRefresh)

    @staticmethod
    def register():
        game.effects.register(Reraise.TUNING.NAME, Reraise)
