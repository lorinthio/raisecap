from core.combat import applyDamage
from core.effect.base import EffectBase
from core.helper import sendMessage
from raisecap.tuning.effect import EffectTuning
from core.util import DamageSource

from siege import game
from siege.network import NetworkManager


class Poison(EffectBase):
    TUNING = EffectTuning.POISON

    def __init__(self, owner, level, duration, source, isRefresh):
        # tick is 3s if poison lasts for 24 seconds then that is 25% life
        if owner.isPlayer() and NetworkManager.isHost():
            for slot in owner.gear.getCategorySlots('accessory'):
                accessory = owner.gear.get(slot).item
                if accessory:
                    if accessory.content.getName() == "poison_charm":
                        sendMessage('general', 'System', "PoisonCharmResist", name=owner.name)
                        return

        super(Poison, self).__init__(owner, duration, isRefresh)
        self.amount = owner.stats.HP.getMax() / (34 - level * 2)

    def update(self, frameTime, owner):
        if NetworkManager.isHost() and game.isOnTick() and owner.combat.isAlive.get():
            applyDamage(owner, self.amount, origin=None, knockback=None, damageSource=DamageSource.Poison)
            # Reset combat time so the player doesn't get out of combat health regen
            owner.combat.timeSinceCombat = 0
        return True

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(Poison.TUNING.NAME, Poison)
