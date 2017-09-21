from functools import partial

from core.combat import AttackType, DamageType
from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege.log import Log


class Focus(EffectBase):
    TUNING = EffectTuning.FOCUS

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Focus, self).__init__(owner, duration, isRefresh)
        self.level = level
        game.events['deal_critical_damage'].listen(partial(self.onDealDamage, owner.id))

    def onRemove(self, owner):
        game.events['deal_critical_damage'].remove(partial(self.onDealDamage, owner.id))

    def onDealDamage(self, ownerId, player, results, attacker, target, data, isCritical, criticalFactor):
        if ownerId == attacker.id and data.attackType in [AttackType.Melee, AttackType.Ranged] and data.damageType is DamageType.Physical:
            results.isCritical = True
            Log.info(str(self.TUNING.AMOUNTS))
            results.criticalFactor += self.TUNING.AMOUNTS[self.level - 1] / 100.0
            attacker.effects.remove(self.TUNING.NAME)

    @staticmethod
    def register():
        game.effects.register(Focus.TUNING.NAME, Focus)
