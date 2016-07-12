from core.effect.base import EffectBase
from raisecap.tuning.skill import SkillTuning
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege import Locale


class Veil(EffectBase):
    TUNING = EffectTuning.VEIL

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Veil, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        self.amount = SkillTuning.VEIL.VEIL_AMOUNTS[level - 1]
        game.events['deal_damage'].listen(self.handleDealDamage)

    def onRemove(self, owner):
        game.events['deal_damage'].remove(self.handleDealDamage)

    def handleDealDamage(self, player, results, attacker, target, data, isCritical, damage):
        if self.ownerId == target.id:
            self.amount -= 1
            results.damage = 0
            # TODO: Consider showing animation on top of target
            if self.amount == 0:
                target.effects.remove(self.name)

    @property
    def description(self):
        return Locale.getEscaped(self.TUNING.DESC).format(count=self.amount)

    @staticmethod
    def register():
        game.effects.register(Veil.TUNING.NAME, Veil)
