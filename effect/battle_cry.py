from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game, Locale


class BattleCry(EffectBase):
    TUNING = EffectTuning.BATTLE_CRY

    @property
    def description(self):
        return Locale.getEscaped(BattleCry.TUNING.DESC).format(stat_buff=(BattleCry.TUNING.AMOUNTS[self.level - 1]))

    def __init__(self, owner, level, duration, source, isRefresh):
        super(BattleCry, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        self.level = level
        stats = owner.stats
        self.uids = {}
        for statName in self.TUNING.STATS:
            self.uids[statName] = stats.get(statName).mod(self.TUNING.AMOUNTS[self.level - 1])

    def onRemove(self, owner):
        stats = owner.stats
        for statName in self.TUNING.STATS:
            stats.get(statName).unmod(self.uids[statName])

    @staticmethod
    def register():
        game.effects.register(BattleCry.TUNING.NAME, BattleCry)
