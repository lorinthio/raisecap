from functools import partial

from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning
from siege import game, Locale
from siege.network import NetworkManager


class Perseverance(EffectBase):
    TUNING = EffectTuning.PERSEVERANCE

    @property
    def description(self):
        return Locale.getEscaped(Perseverance.TUNING.DESC).format(xpBonus=Perseverance.TUNING.XP_BONUS, tpBonus=Perseverance.TUNING.TP_BONUS)

    def __init__(self, owner, level, duration, source, isRefresh):
        owner.event['gain_tp'].listen(self.handleGainTp)
        owner.event['gain_xp'].listen(self.handleGainXp)

    def onRemove(self, owner):
        owner.event['gain_tp'].remove(self.handleGainTp)
        owner.event['gain_xp'].remove(self.handleGainXp)

    def handleGainTp(self, player, result, talent, amount):
        result.amount += int(amount * (Perseverance.TUNING.TP_BONUS / 100.0))

    def handleGainXp(self, player, result, amount):
        result.amount += int(amount * (Perseverance.TUNING.XP_BONUS) / 100.0)

    @staticmethod
    def apply(player):
        player.entity.effects.add(Perseverance.TUNING.NAME, 1, 0)
        player.entity.playerState.perseveranceTimerJob = 0

    @staticmethod
    def handlePlayerRespawn(player):
        player.entity.effects.remove(Perseverance.TUNING.NAME)
        playerState = player.entity.playerState
        existingJob = playerState.perseveranceTimerJob
        if existingJob:
            game.timer.cancel(existingJob)
        playerState.perseveranceTimerJob = game.timer.add(Perseverance.TUNING.TIME, partial(Perseverance.apply, player))

    @staticmethod
    def handlePlayerJoined(player):
        if not player.entity.effects.has(Perseverance.TUNING.NAME):
            playerState = player.entity.playerState
            playerState.perseveranceTimerJob = game.timer.add(playerState.perseveranceTime, partial(Perseverance.apply, player))

    @staticmethod
    def register():
        game.effects.register(Perseverance.TUNING.NAME, Perseverance)
        if NetworkManager.isHost():
            game.events['player_respawn'].listen(Perseverance.handlePlayerRespawn)
            game.events['player_joined'].listen(Perseverance.handlePlayerJoined)

    @staticmethod
    def unregister():
        if NetworkManager.isHost():
            game.events['player_respawn'].remove(Perseverance.handlePlayerRespawn)
            game.events['player_joined'].remove(Perseverance.handlePlayerJoined)
