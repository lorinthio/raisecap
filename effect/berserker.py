from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game, Locale


class Berserker(EffectBase):
    TUNING = EffectTuning.BERSERKER

    @property
    def description(self):
        return Locale.getEscaped(Berserker.TUNING.DESC).format(stat=Locale.getEscaped(self.statName), statBonus=(Berserker.TUNING.STAT_BONUS * self.level))

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Berserker, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        self.level = level
        stat = owner.stats.get(Berserker.TUNING.STAT)
        self.statUid = stat.mod((self.level * Berserker.TUNING.STAT_BONUS) / 100.0, isMultiplier=True)
        self.statName = stat.fullName

    def onRemove(self, owner):
        owner.stats.get(Berserker.TUNING.STAT).unmod(self.statUid)

    @staticmethod
    def register():
        game.effects.register(Berserker.TUNING.NAME, Berserker)
