from core.helper import convertTimeToString, sendMessage
from raisecap.tuning.effect import EffectTuning
from siege import Locale


class EffectBase(object):
    TUNING = EffectTuning.BASE

    def __init__(self, owner, duration, isRefresh):
        if not isRefresh:
            sendMessage('battle', 'System', "StatusEffect", effect=self.name, name=owner.name, duration=convertTimeToString(duration))

    @property
    def name(self):
        return self.TUNING.NAME

    @property
    def icon(self):
        return self.TUNING.ICON

    @property
    def description(self):
        return Locale.getEscaped(self.TUNING.DESC)

    def removeOnDeath(self):
        return True

    def isPositive(self):
        return True
