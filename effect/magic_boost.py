from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game


class MagicBoost(EffectBase):
    # Only set up to work on player at the moment.
    TUNING = EffectTuning.MAGIC_BOOST

    def __init__(self, owner, level, duration, source, isRefresh):
        super(MagicBoost, self).__init__(owner, duration, isRefresh)
        self.magicBoost = self.TUNING.AMOUNTS[level]
        owner.event['deal_damage_start'].listen(self.onDealDamage)

    def onRemove(self, owner):
        owner.event['deal_damage_start'].remove(self.onDealDamage)

    def onDealDamage(self, player, results, attacker, target, data):
        data.power += self.magicBoost
        player.entity.effects.remove(self.TUNING.NAME)

    def read(self, stream):
        stream.readUint8()  # Unused sadly but must remain for backwards compatability for the time being

    def write(self, stream):
        stream.writeUint8(0)

    @staticmethod
    def register():
        game.effects.register(MagicBoost.TUNING.NAME, MagicBoost)
