from functools import partial

from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game


class Empowerment(EffectBase):
    TUNING = EffectTuning.EMPOWERMENT

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Empowerment, self).__init__(owner, duration, isRefresh)
        self.level = level
        game.events['deal_critical_damage'].listen(partial(self.onDealDamage, owner.id))

    def onRemove(self, owner):
        game.events['deal_critical_damage'].remove(partial(self.onDealDamage, owner.id))

    def onDealDamage(self, ownerId, player, results, attacker, target, data, isCritical, criticalFactor):
        if ownerId == attacker.id and data.source is 'syle':
            results.isCritical = True
            results.criticalFactor = self.TUNING.AMOUNT / 100.0
            attacker.effects.remove(self.TUNING.NAME)

    @staticmethod
    def register():
        game.effects.register(Empowerment.TUNING.NAME, Empowerment)
