from core.effect.base import EffectBase
from raisecap.tuning.skill import SkillTuning
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege import Locale


class Stoneskin(EffectBase):
    TUNING = EffectTuning.STONESKIN

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Stoneskin, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        self.life = SkillTuning.STONESKIN.ABSORBED_AMOUNTS[level - 1]
        game.events['apply_damage'].listen(self.handleApplyDamage)

    def onRemove(self, owner):
        game.events['apply_damage'].remove(self.handleApplyDamage)

    def handleApplyDamage(self, player, results, target, origin, damage, isCritical, knockback):
        if self.ownerId == target.id:
            protection = min(self.life, results.damage)
            self.life -= protection
            results.damage -= protection
            # TODO: Consider showing animation on top of target
            if not self.life:
                target.effects.remove(self.name)

    @property
    def description(self):
        return Locale.getEscaped(self.TUNING.DESC).format(life=int(self.life))

    @staticmethod
    def register():
        game.effects.register(Stoneskin.TUNING.NAME, Stoneskin)
