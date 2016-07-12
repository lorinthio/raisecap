from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game, Locale


class StatLoss(EffectBase):
    TUNING = EffectTuning.STAT_LOSS
    STAT = ""

    @property
    def name(self):
        return Locale.getEscaped(self.TUNING.NAME).format(stat=self.statName)

    @property
    def icon(self):
        return self.ICON

    @property
    def description(self):
        return Locale.getEscaped(self.TUNING.DESC).format(stat=self.statName, statLoss=(self.TUNING.AMOUNT * self.level))

    def __init__(self, owner, level, duration, source, isRefresh):
        self.ownerId = owner.id
        stat = owner.stats.get(self.STAT)
        self.statName = stat.fullName
        self.level = level

        super(StatLoss, self).__init__(owner, duration, isRefresh)

        self.statUid = stat.mod(int(stat.get() * (self.TUNING.AMOUNT / 100.0) * level))

    def onRemove(self, owner):
        owner.stats.get(self.STAT).unmod(self.statUid)

    def read(self, stream):
        value = stream.readUint8()
        if value != 0:
            owner = game.entity.get(self.ownerId)
            stat = owner.stats.get(self.STAT)
            if stat.hasMax():
                stat.adjustMax(-value)
            else:
                stat.adjust(-value)

    def write(self, stream):
        stream.writeUint8(0)  # FILE_VERSIONING 0.30.2

    def isPositive(self):
        return False

    @staticmethod
    def register():
        for stat in StatLoss.TUNING.STATS:
            name = "{}StatLoss".format(stat.capitalize())
            info = {
                'NAME': name,
                'ICON': "mods/core/effect/stat_loss_{}.png".format(stat.lower()),
                'STAT': stat
            }
            game.effects.register(name, type(name, (StatLoss,), info))
