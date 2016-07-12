from functools import partial

from core.combat import applyDamage
from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from core.util import DamageSource

from siege import game, Locale
from siege.network import NetworkManager


class Corruption(EffectBase):
    TUNING = EffectTuning.CORRUPTION

    @property
    def description(self):
        return Locale.getEscaped(Corruption.TUNING.DESC)

    def __init__(self, owner, level, duration, source, isRefresh):
        self.amount = owner.stats.HP.getMax() * (Corruption.TUNING.PERCENTAGE_PER_TICK / 100.00)
        if owner.isPlayer():
            game.events['heal_entity'].listen(partial(self.handleHeal, owner.id))
            owner.event['hp_regen'].listen(partial(self.handleHpRegen, owner.id))

    def onRemove(self, owner):
        if owner.isPlayer():
            game.events['heal_entity'].remove(partial(self.handleHeal, owner.id))
            owner.event['hp_regen'].remove(partial(self.handleHpRegen, owner.id))

    def update(self, frameTime, owner):
        if game.isOnTick() and NetworkManager.isHost():
            applyDamage(owner, self.amount, origin=None, knockback=None, damageSource=DamageSource.Burning)
            if owner.has("combat"):
                owner.combat.timeSinceCombat = 0
        return True

    def handleHeal(self, entityId, player, results, user, target, amount):
        if entityId == target.id:
            results.amount = 0

    def handleHpRegen(self, entityId, player, results, hpRegenTotal):
        if entityId == player.entity.id:
            results.hpRegenTotal = 0

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Corruption.TUNING.NAME, Corruption)
