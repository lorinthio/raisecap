from core.helper import AttrDict
from raisecap.tuning.skill import DamageType, SkillTuning
from siege.util import minutes, RangeInt, seconds


class EffectTuning(object):

    BASE = AttrDict(NAME="", ICON="", DESC="")

    BATTLE_CRY = AttrDict(
        NAME = SkillTuning.BATTLE_CRY.NAME,
        ICON = SkillTuning.BATTLE_CRY.ICON,
        DESC = "BattleCryDesc",
        STATS = ['ATK', 'DEF', 'AGI'],
        AMOUNTS = SkillTuning.BATTLE_CRY.STAT_BUFFS,
    )

    BERSERK = AttrDict(
        NAME = SkillTuning.BERSERK.NAME,
        ICON = SkillTuning.BERSERK.ICON,
        DESC = "BerserkDesc",
        STATS = ['ATK', 'AGI'],
        SP_DRAINS = [10, 9, 9, 9, 8, 8, 8, 7, 7, 7],
        AMOUNTS = SkillTuning.BERSERK.STAT_BUFFS,
    )

    BERSERKER = AttrDict(
        NAME = "Berserker",
        DESC = "BerserkerDesc",
        ICON = "mods/core/item/weapon/spear/halberd_icon.png",
        STAT = "ATK",
        TIME = seconds(5),
        STAT_BONUS = 4,  # Percentage
        MAX_LEVEL = 5,
    )

    BLIND = AttrDict(
        NAME = "Blind",
        ICON = "mods/core/effect/blind.png",
        DESC = "BlindDesc",
        AMOUNT = 20
    )

    BLOOD_RAIN = AttrDict(
        NAME = "BloodRainEffect",
        ICON = "mods/core/effect/poison.png",
        DESC = "BloodRainEffectDesc",
    )

    BREATHLESS = AttrDict(
        NAME = "Breathless",
        ICON = "mods/core/effect/blind.png",
        DESC = "BreathlessDesc",
        AMOUNT = 10,
        TIME = seconds(8)
    )

    BURN = AttrDict(
        NAME = "Burn",
        ICON = "mods/core/effect/burn.png",
        DESC = "BurnDesc",
        PERCENTAGE_PER_TICK = 7,
        TIME = seconds(10)
    )

    CHAOS_BURN = AttrDict(
        NAME = "ChaosBurn",
        ICON = "mods/core/item/armor/accessory/core_of_chaos.png",
        DESC = "ChaosBurnDesc",
        PERCENTAGE_PER_TICK = 5,
        TIME = seconds(10),
    )

    CORRUPTION = AttrDict(
        NAME = "Corruption",
        ICON = "mods/core/effect/corruption.png",
        DESC = "CorruptionDesc",
        PERCENTAGE_PER_TICK = 5,
        TIME = seconds(10),
    )

    DEFENSE_BREAK = AttrDict(
        NAME = "DefenseBreak",
        DESC = "DefenseBreakDesc",
        ICON = "mods/core/item/weapon/spear/halberd_icon.png",
        STAT = "DEF",
        TIME = seconds(5),
        PERCENTAGE = 4,  # Percentage
        MAX_LEVEL = 5,
    )

    EXHAUSTED = AttrDict(
        NAME = "Exhausted",
        ICON = "mods/core/effect/exhausted.png",
        DESC = "ExhaustedDesc"
    )

    FROSTBITE = AttrDict(
        NAME = "Frostbite",
        ICON = "mods/core/effect/frostbite.png",
        DESC = "FrostbiteDesc",
        AMOUNT = 5,
        TIME = seconds(10)
    )

    FIRESTORM = AttrDict(
        NAME = "Firestorm",
        ICON = "mods/core/talent/syle/enshroud_aegnix_icon.png",
        DESC = "FirestormEffectDesc",
        STAMINA_REGEN = 10,
        STAMINA_REGEN_LEVEL = 10
    )

    HASTE = AttrDict(
        NAME = SkillTuning.HASTE.NAME,
        ICON = SkillTuning.HASTE.ICON,
        DESC = SkillTuning.HASTE.NAME + "EffectDesc",
    )

    INCREASE_DROP_RATE = AttrDict(
        NAME = "IncreaseDropRate",
        ICON = "mods/core/effect/increase_drop_rate.png",
        DESC = "IncreaseDropRateDesc",
    )

    INVIGORATED = AttrDict(
        NAME = "Invigorated",
        ICON = SkillTuning.HEAL.ICON,
        DESC = "InvigoratedDesc",
        AMOUNT = 10,
        TIME = seconds(10),
    )

    INVINCIBLE = AttrDict(
        NAME = "Invincible",
        ICON = "mods/core/effect/invincible.png",
        DESC = "InvincibleDesc",
    )

    INVISIBLE = AttrDict(
        NAME = SkillTuning.INVISIBLE.NAME,
        ICON = SkillTuning.INVISIBLE.ICON,
        DESC = SkillTuning.INVISIBLE.NAME + "EffectDesc"
    )

    MAGIC_BOOST = AttrDict(
        NAME = "MagicBoost",
        ICON = "mods/core/effect/magic_boost.png",
        DESC = "MagicBoostDesc",
        AMOUNTS = [5, 10, 15, 20, 25]
    )

    PARALYZE = AttrDict(
        NAME = "Paralyze",
        ICON = "mods/core/effect/stun.png",
        DESC = "ParalyzeDesc",
        NEXT_PARALYSIS = RangeInt(seconds(2), seconds(3)),
    )

    PERSEVERANCE = AttrDict(
        NAME = "Perseverance",
        ICON = "mods/core/effect/perseverance.png",
        DESC = "PerseveranceDesc",
        TIME = minutes(30),
        XP_BONUS = 20,  # Percentage
        TP_BONUS = 20  # Percentage
    )

    POISON = AttrDict(
        NAME = "Poison",
        ICON = "mods/core/effect/poison.png",
        DESC = "PoisonDesc",
    )

    PRECISION = AttrDict(
        NAME = "PrecisionEffect",
        ICON = "mods/core/talent/gather/precision_icon.png",
        DESC = "PrecisionEffectDesc",
    )

    FOCUS = AttrDict(
        NAME = SkillTuning.FOCUS.NAME,
        ICON = SkillTuning.FOCUS.ICON,
        DESC = SkillTuning.FOCUS.NAME + "EffectDesc",
        AMOUNTS = SkillTuning.FOCUS.CRITICAL_MODIFIERS,
    )

    EMPOWERMENT = AttrDict(
        NAME = "Empowerment",
        ICON = SkillTuning.WAND_PROFICIENCY.ICON,
        DESC = "EmpowermentDesc",
        AMOUNT = 150,
    )

    PROTECT = AttrDict(
        NAME = SkillTuning.PROTECT.NAME,
        ICON = SkillTuning.PROTECT.ICON,
        DESC = SkillTuning.PROTECT.NAME + "EffectDesc"
    )

    REGEN = AttrDict(
        NAME = "Regen",
        ICON = SkillTuning.REGENERATE.ICON,
        DESC = "RegenDesc"
    )

    RERAISE = AttrDict(
        NAME = "Reraise",
        ICON = "mods/core/effect/reraise.png",
        DESC = "ReraiseDesc",
        HEALTH = [25, 50, 75, 100, 100]  # Percentage of health recovered when revived
    )

    SANDSTORM = AttrDict(
        NAME = "Sandstorm",
        ICON = "mods/core/talent/syle/enshroud_silvan_icon.png",
        DESC = "SandstormEffectDesc",
        STAMINA_REGEN = 10,
        STAMINA_REGEN_LEVEL = 10
    )

    SHELL = AttrDict(
        NAME = SkillTuning.SHELL.NAME,
        ICON = SkillTuning.SHELL.ICON,
        DESC = SkillTuning.SHELL.NAME + "EffectDesc"
    )

    SILENCE = AttrDict(
        NAME = "Silence",
        ICON = "mods/core/effect/silence.png",
        DESC = "SilenceDesc"
    )

    SNARE = AttrDict(
        NAME = "Snare",
        ICON = "mods/core/effect/exhausted.png",
        DESC = "SnareDesc"
    )

    SNOWSTORM = AttrDict(
        NAME = "Snowstorm",
        ICON = "mods/core/talent/syle/enshroud_lacies_icon.png",
        DESC = "SnowstormEffectDesc",
        STAMINA_REGEN = 10,
        STAMINA_REGEN_LEVEL = 10
    )

    STAT_BOOST = AttrDict(
        NAME = "StatBoost",
        DESC = "StatBoostDesc",
        AMOUNT = 5,  # Percentage
        STATS = ['HP', 'SP', 'ATK', 'DEF', 'INT', 'MIND', 'AGI', 'LUCK', 'SPD'],
    )

    STAT_LOSS = AttrDict(
        NAME = "StatLoss",
        DESC = "StatLossDesc",
        AMOUNT = -5,  # Percentage
        STATS = ['MIND'],
    )

    STONESKIN = AttrDict(
        NAME = SkillTuning.STONESKIN.NAME,
        ICON = SkillTuning.STONESKIN.ICON,
        DESC = SkillTuning.STONESKIN.NAME + "EffectDesc"
    )

    STUN = AttrDict(
        NAME = "Stun",
        ICON = "mods/core/effect/stun.png",
        DESC = "StunEffectDesc"
    )

    VEIL = AttrDict(
        NAME = SkillTuning.VEIL.NAME,
        ICON = SkillTuning.VEIL.ICON,
        DESC = SkillTuning.VEIL.NAME + "EffectDesc"
    )

    WEIGHTED = AttrDict(
        NAME = "Weighted",
        ICON = "mods/core/effect/weighted.png",
        DESC = "WeightedDesc",
        AMOUNT = 20,
        TIME = seconds(3)
    )

    WINDSTORM = AttrDict(
        NAME = "Windstorm",
        ICON = "mods/core/talent/syle/enshroud_aeolus_icon.png",
        DESC = "WindstormEffectDesc",
        STAMINA_REGEN = 10,
        STAMINA_REGEN_LEVEL = 10
    )

    ELEMENT_CHANCE = 20
    ELEMENT_EFFECTS = {
        DamageType.Fire: BURN,
        DamageType.Water: FROSTBITE,
        DamageType.Wind: BREATHLESS,
        DamageType.Earth: WEIGHTED
    }
