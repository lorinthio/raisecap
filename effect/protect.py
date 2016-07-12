from core.combat import AttackType
from core.effect.base import EffectBase
from core.tuning.skill import SkillTuning
from raisecap.tuning.effect import EffectTuning
from siege import game


class Protect(EffectBase):
    TUNING = EffectTuning.PROTECT

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Protect, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        self.percentage = SkillTuning.PROTECT.NEGATED_AMOUNTS[level - 1]
        game.events['deal_damage'].listen(self.handleDealDamage)

    def onRemove(self, owner):
        game.events['deal_damage'].remove(self.handleDealDamage)

    def handleDealDamage(self, player, results, attacker, target, data, isCritical, damage):
        if data.attackType is AttackType.Melee and self.ownerId == target.id:
            results.damage -= results.damage * self.percentage / 100.0
            # TODO: Consider showing animation on top of target

    @staticmethod
    def register():
        game.effects.register(Protect.TUNING.NAME, Protect)
