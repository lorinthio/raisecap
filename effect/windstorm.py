from core.effect.base import EffectBase
from core.talent.syle import EnshroudForm
from raisecap.tuning.effect import EffectTuning
from raisecap.tuning.skill import SkillTuning

from siege import game
from siege.network import NetworkManager


class Windstorm(EffectBase):
    TUNING = EffectTuning.WINDSTORM

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Windstorm, self).__init__(owner, duration, isRefresh)
        self.level = level
        self.duration = duration
        if NetworkManager.isHost() and owner.realm:
            self.addStorm(owner)
        else:
            self.ownerId = owner.id
            self.storm = None

        if self.level >= self.TUNING.STAMINA_REGEN_LEVEL:
            self.statUid = owner.stats.SPRegen.mod(self.TUNING.STAMINA_REGEN)

    def addStorm(self, owner):
        tuning = SkillTuning.combine(SkillTuning.ENSHROUD_FORM, 'ENSHROUD_FORM_AEOLUS')
        powerUp = True if self.duration == SkillTuning.ENSHROUD_FORM.POWER_UP_DURATION else False
        self.storm = EnshroudForm._createStormEntity(owner, self.level, 'enshroud_aeolus', tuning, powerUp)
        for effect in [EffectTuning.FIRESTORM.NAME, EffectTuning.SANDSTORM.NAME, EffectTuning.SNOWSTORM.NAME]:
            owner.effects.remove(effect)

    def onRemove(self, owner):
        if NetworkManager.isHost() and self.storm is not None:
            self.storm.destroy()

        if self.level >= self.TUNING.STAMINA_REGEN_LEVEL:
            owner.stats.SPRegen.unmod(self.statUid)

    def read(self, stream):
        game.events['player_joined'].listen(self._playerJoined)

    def _playerJoined(self, player):
        if player.entity.id == self.ownerId:
            self.addStorm(player.entity)
        return True

    @staticmethod
    def register():
        game.effects.register(Windstorm.TUNING.NAME, Windstorm)
