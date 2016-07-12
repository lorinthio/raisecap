from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game, Locale


class DefenseBreak(EffectBase):
    TUNING = EffectTuning.DEFENSE_BREAK

    @property
    def description(self):
        return Locale.getEscaped(DefenseBreak.TUNING.DESC).format(stat=Locale.getEscaped(self.statName), statBonus=(DefenseBreak.TUNING.PERCENTAGE * self.level))

    def __init__(self, owner, level, duration, source, isRefresh):
        super(DefenseBreak, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        self.level = level
        stat = owner.stats.get(DefenseBreak.TUNING.STAT)
        self.statUid = stat.mod(-(self.level * DefenseBreak.TUNING.PERCENTAGE) / 100.0, isMultiplier=True)
        self.statName = stat.fullName

    def onRemove(self, owner):
        owner.stats.get(DefenseBreak.TUNING.STAT).unmod(self.statUid)

    def isPositive(self):
        return False

    @staticmethod
    def register():
        game.effects.register(DefenseBreak.TUNING.NAME, DefenseBreak)
