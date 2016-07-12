from core.effect.base import EffectBase
from raisecap.tuning.effect import EffectTuning

from siege import game
from siege.network import NetworkManager
from siege.world import World


class Invisible(EffectBase):
    TUNING = EffectTuning.INVISIBLE
    FRIENDLY_ALPHA = 128
    ENEMY_ALPHA = 4

    def __init__(self, owner, level, duration, source, isRefresh):
        super(Invisible, self).__init__(owner, duration, isRefresh)
        self.ownerId = owner.id
        owner.combat.isTargetable.set(False)
        if owner.has('physics') and not NetworkManager.isStandalone():
            player = World.get().getPlayer()
            self.alpha = Invisible.FRIENDLY_ALPHA if not player or player.entity.combat.team == owner.combat.team else Invisible.ENEMY_ALPHA
            owner.physics.onTimeStep.listen(self.handleUpdate)
        game.events['deal_damage_end'].listen(self.handleDealDamageEnd)

    def onRemove(self, owner):
        owner.combat.isTargetable.set(True)
        if not NetworkManager.isStandalone():
            if owner.render.alpha == self.alpha:
                owner.render.alpha = 255
            if owner.has('physics'):
                owner.physics.onTimeStep.remove(self.handleUpdate)
        game.events['deal_damage_end'].remove(self.handleDealDamageEnd)

    def handleUpdate(self, physics, timestepTime):
        physics.getParent().render.alpha = self.alpha

    def handleDealDamageEnd(self, player, results, attacker, target, data, isCritical, damage):
        if player:
            player.entity.event['deal_damage_invisible'].invoke(target, data, isCritical, damage)
        if self.ownerId == attacker.id:
            attacker.effects.remove(self.name)
        elif self.ownerId == target.id:
            target.effects.remove(self.name)

    @staticmethod
    def register():
        game.effects.register(Invisible.TUNING.NAME, Invisible)
