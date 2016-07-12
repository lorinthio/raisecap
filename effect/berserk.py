from core.effect.battle_cry import BattleCry
from raisecap.tuning.effect import EffectTuning
from siege import game, Locale


class Berserk(BattleCry):
    TUNING = EffectTuning.BERSERK

    @property
    def description(self):
        return Locale.getEscaped(Berserk.TUNING.DESC).format(sp_drain=Berserk.TUNING.SP_DRAINS[self.level - 1], stat_buff=Berserk.TUNING.AMOUNTS[self.level - 1])

    def onRemove(self, owner):
        super(Berserk, self).onRemove(owner)
        owner.combat.canRecover.set(True)

    def read(self, stream):
        game.events['player_joined'].listen(self._playerJoined)

    def _playerJoined(self, player):
        if player.entity.id == self.ownerId:
            player.entity.effects.remove(Berserk.TUNING.NAME)
        return True

    @staticmethod
    def register():
        game.effects.register(Berserk.TUNING.NAME, Berserk)
