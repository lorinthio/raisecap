from core.helper import AttrDict
from core.util import enum
from siege.graphic import Color
from siege.util import minutes, seconds
from siege.log import Log

from core.tuning.skill import SkillTuning as st

DamageType = enum("Physical", "Fire", "Earth", "Wind", "Water", "All")
AttackType = enum("Divine", "Melee", "Magic", "Ranged", "All")


def register():
    SkillTuning.run()


class SkillTuning(object):

    @staticmethod
    def combine(base, *args):
        result = AttrDict(base)
        for arg in args:
            if hasattr(SkillTuning, arg):
                result.update(getattr(SkillTuning, arg))
        return result

    # Syle Channeling Skills
    CHANNEL_AEGNIX = AttrDict(
        TYPE = "Aegnix",
        NAME = "ChannelAegnix",
        ICON = "mods/core/talent/syle/channel_aegnix_icon.png",
        PARTICLE_PATH = "mods/core/talent/syle/fire_particle.png",
        LIGHT_COLOR = Color(240, 200, 160),
        ATTACK_TYPE = AttackType.Magic,
        DAMAGE_TYPE = DamageType.Fire,
        ELEMENT = 'fire',
        STATUS_EFFECT = 'Burn',
        CHANNEL_SOUND = "mods/core/audio/sfx/channel/aegnix.ogg"
    )
    CHANNEL_AEOLUS = AttrDict(
        TYPE = "Aeolus",
        NAME = "ChannelAeolus",
        ICON = "mods/core/talent/syle/channel_aeolus_icon.png",
        LIGHT_COLOR = Color(173, 241, 203),
        ATTACK_TYPE = AttackType.Magic,
        DAMAGE_TYPE = DamageType.Wind,
        ELEMENT = 'wind',
        STATUS_EFFECT = 'Breathless',
        CHANNEL_SOUND = "mods/core/audio/sfx/channel/aeolus.ogg"
    )
    CHANNEL_LACIES = AttrDict(
        TYPE = "Lacies",
        NAME = "ChannelLacies",
        ICON = "mods/core/talent/syle/channel_lacies_icon.png",
        PARTICLE_PATH = "mods/core/talent/syle/blizzard_particle.png",
        LIGHT_COLOR = Color(115, 200, 236),
        ATTACK_TYPE = AttackType.Magic,
        DAMAGE_TYPE = DamageType.Water,
        ELEMENT = 'water',
        STATUS_EFFECT = 'Frostbite',
        CHANNEL_SOUND = "mods/core/audio/sfx/channel/lacies.ogg"
    )
    CHANNEL_SILVAN = AttrDict(
        TYPE = "Silvan",
        NAME = "ChannelSilvan",
        ICON = "mods/core/talent/syle/channel_silvan_icon.png",
        PARTICLE_PATH = "mods/core/talent/syle/stone_particle.png",
        LIGHT_COLOR = Color(241, 193, 173),
        ATTACK_TYPE = AttackType.Magic,
        DAMAGE_TYPE = DamageType.Earth,
        ELEMENT = 'earth',
        STATUS_EFFECT = 'Weighted',
        CHANNEL_SOUND = "mods/core/audio/sfx/channel/silvan.ogg"
    )
    CHANNEL_TYPES = [
        CHANNEL_AEGNIX,
        CHANNEL_LACIES,
        CHANNEL_AEOLUS,
        CHANNEL_SILVAN,
    ]

    # Syle Skills
    WAND_PROFICIENCY = AttrDict(
        NAME = "WandProficiency",
        DESCRIPTION = "WandProficiencyDesc",
        ICON = "mods/core/talent/syle/wand_proficiency_icon.png",
        UNLOCK_LEVELS = [1, 7, 14, 22, 30],
        LEVEL_COSTS = [400, 450, 500, 600, 700],
    )

    INTELLIGENCE_BOOST = AttrDict(
        NAME = "IntelligenceBoost",
        DESCRIPTION = "IntelligenceBoostDesc",
        ICON = "mods/core/talent/syle/intelligence_boost_icon.png",
        UNLOCK_LEVELS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 50, 55, 60, 66, 72, 78, 85, 92, 99],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 700, 700, 800, 800, 900, 900, 900, 1000],
        STAT = 'INT',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 74, 80]
    )

    # # st.INTELLIGENCE_BOOST = INTELLIGENCE_BOOST

    MIND_BOOST = AttrDict(
        NAME = "MindBoost",
        DESCRIPTION = "MindBoostDesc",
        ICON = "mods/core/talent/syle/mind_boost_icon.png",
        UNLOCK_LEVELS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 50, 55, 60, 66, 72, 78, 85, 92, 99],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 700, 700, 800, 800, 900, 900, 900, 1000],
        STAT = 'MIND',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 74, 80]
    )

    # # st.MIND_BOOST = MIND_BOOST

    BASE_POWER = {
        0: 12,
        1: 16,
        2: 20,
        3: 24,
        4: 28,
        5: 32,
        6: 38,
        7: 42,
        8: 46,
        9: 50
    }

    HEAL = AttrDict(
        NAME = "Heal",
        DESCRIPTION = "HealDesc",
        ICON = "mods/core/talent/syle/heal_spell_icon.png",
        UNLOCK_LEVELS = [1, 1, 7, 11, 15, 19, 23, 27, 31, 35, 40, 46, 52, 58, 65, 72, 80, 90],
        LEVEL_COSTS = [0, 350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 500, 600],
        CAST_TIME = 800,
        COOLDOWN = seconds(8),
        SP_COSTS = [60, 50, 50, 45, 45, 45, 40, 40, 40, 35, 35, 35, 35, 30, 30, 30, 30, 30],
        TP_AMOUNT = 25,
        TP_CHANCE = 50,
        STATUS_EFFECT_CHANCES = [0, 0, 0, 0, 20, 20, 20, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40],
        SOUND = "mods/core/audio/sfx/talent/syle/heal.ogg",
        SOUND_TIMING = 350,
        RANGE = 224,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 168, 168],
        HP_AMOUNTS = [40, 40, 50, 50, 50, 70, 70, 70, 110, 110, 110, 140, 140, 140, 140, 170, 170, 170],
    )

    BASE_FORM = AttrDict(
        NAME = "BaseForm",
        TYPE = "Base",
        DESCRIPTION = "BaseFormDesc",
        ICON = "mods/core/talent/syle/base_icon.png",
        ICON_TEMPLATE = "mods/core/talent/syle/base_{}_icon.png",
        UNLOCK_LEVELS = [1, 1, 4, 9, 13, 17, 21, 25, 29, 33, 37, 42, 48, 54, 60, 68, 74, 84, 95],
        LEVEL_COSTS = [0, 350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 500, 600, 600],
        CAST_TIME = 500,
        COOLDOWN = seconds(3),
        POWERS = [120, 120, 126, 126, 126, 135, 135, 135, 145, 145],
        SP_COSTS = [45, 40, 40, 35, 35, 35, 30, 30, 30, 25],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        STATUS_EFFECT_CHANCES = [0, 0, 0, 0, 20, 20, 20, 40, 40, 40],
        SOUND = "mods/core/audio/sfx/talent/syle/fire.ogg",
        SOUND_TIMING = 300
    )
    BASE_FORM_AEGNIX = AttrDict(NAME="FireballSpell", PARTICLE_PATH="mods/core/talent/syle/fire_particle.png", SOUND="mods/core/audio/sfx/talent/syle/fire.ogg")
    BASE_FORM_LACIES = AttrDict(NAME="BlizzardSpell", PARTICLE_PATH="mods/core/talent/syle/blizzard_particle.png", SOUND="mods/core/audio/sfx/talent/syle/blizzard.ogg")
    BASE_FORM_AEOLUS = AttrDict(NAME="AeroSpell", PARTICLE_PATH="mods/core/talent/syle/wind_particle.png", SOUND="mods/core/audio/sfx/talent/syle/aero.ogg")
    BASE_FORM_SILVAN = AttrDict(NAME="StoneSpell", PARTICLE_PATH="mods/core/talent/syle/stone_particle.png", SOUND="mods/core/audio/sfx/talent/syle/stone.ogg")

    PILLAR_FORM = AttrDict(
        NAME = "PillarForm",
        TYPE = "Pillar",
        DESCRIPTION = "PillarFormDesc",
        ICON = "mods/core/talent/syle/pillar_icon.png",
        ICON_TEMPLATE = "mods/core/talent/syle/pillar_{}_icon.png",
        UNLOCK_LEVELS = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 41, 47, 53, 59, 67, 73, 83, 94],
        LEVEL_COSTS = [0, 350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 500, 600, 600],
        RANGES = [180, 240, 240, 240, 300, 300, 300, 360, 360, 360],
        CAST_TIME = 600,
        COOLDOWN = seconds(8),
        POWERS = [144, 144, 144, 150, 150, 150, 161, 161, 161, 175],
        POWER_UP_LEVEL = 5,
        POWER_UP_POTENCY = 0.7,
        SP_COSTS = [52, 52, 47, 47, 47, 42, 42, 42, 37, 37],
        TP_AMOUNT = 30,
        TP_CHANCE = 35,
        SOUND = "mods/core/audio/sfx/talent/syle/flare.ogg"
    )
    PILLAR_FORM_AEGNIX = AttrDict(NAME="FlareSpell", SOUND="mods/core/audio/sfx/talent/syle/flare.ogg")
    PILLAR_FORM_LACIES = AttrDict(NAME="FreezeSpell", SOUND="mods/core/audio/sfx/talent/syle/freeze.ogg")
    PILLAR_FORM_AEOLUS = AttrDict(NAME="TornadoSpell", SOUND="mods/core/audio/sfx/talent/syle/tornado.ogg")
    PILLAR_FORM_SILVAN = AttrDict(NAME="UpheavalSpell", SOUND="mods/core/audio/sfx/talent/syle/upheaval.ogg")

    PROTECT = AttrDict(
        NAME = "Protect",
        DESCRIPTION = "ProtectDesc",
        ICON = "mods/core/talent/syle/protect_spell_icon.png",
        UNLOCK_LEVELS = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 43, 49, 55, 61, 69, 75, 85, 96],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 500, 500, 500, 550, 550, 550, 600],
        CAST_TIME = 800,
        RANGE = 224,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 168, 168],
        COOLDOWN = seconds(60),
        SP_COSTS = [54, 50, 50, 50, 46, 46, 46, 42, 42, 42, 38, 38, 38, 35, 35, 35, 30, 30],
        BUFF_DURATIONS = [seconds(180), seconds(180), seconds(210), seconds(210), seconds(210), seconds(240), seconds(240), seconds(240), seconds(270), seconds(270), seconds(270), seconds(300), seconds(300), seconds(360), seconds(360), seconds(420), seconds(480), seconds(600)],
        TP_AMOUNT = 25,
        TP_CHANCE = 50,
        NEGATED_AMOUNTS = [10, 10, 10, 14, 14, 14, 18, 18, 18, 24, 24, 24, 28, 28, 28, 33, 33, 33],
        SOUND = "mods/core/audio/sfx/talent/syle/protect.ogg",
        SOUND_TIMING = 350
    )

    #

    SHELL = AttrDict(
        NAME = "Shell",
        DESCRIPTION = "ShellDesc",
        ICON = "mods/core/talent/syle/shell_spell_icon.png",
        UNLOCK_LEVELS = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 43, 49, 55, 61, 69, 75, 85, 96],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 500, 500, 500, 550, 550, 550, 600],
        CAST_TIME = 800,
        RANGE = 224,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 168, 168],
        COOLDOWN = seconds(60),
        SP_COSTS = [54, 50, 50, 50, 46, 46, 46, 42, 42, 42, 38, 38, 38, 35, 35, 35, 30, 30],
        BUFF_DURATIONS = [seconds(180), seconds(180), seconds(210), seconds(210), seconds(210), seconds(240), seconds(240), seconds(240), seconds(270), seconds(270), seconds(270), seconds(300), seconds(300), seconds(360), seconds(360), seconds(420), seconds(480), seconds(600)],
        TP_AMOUNT = 25,
        TP_CHANCE = 50,
        NEGATED_AMOUNTS = [10, 10, 10, 14, 14, 14, 18, 18, 18, 24, 24, 24, 28, 28, 28, 33, 33, 33],
        SOUND = "mods/core/audio/sfx/talent/syle/shell.ogg",
        SOUND_TIMING = 350
    )

    ENSHROUD_FORM = AttrDict(
        NAME = "EnshroudForm",
        TYPE = "Enshroud",
        DESCRIPTION = "EnshroudFormDesc",
        ICON = "mods/core/talent/syle/enshroud_icon.png",
        ICON_TEMPLATE = "mods/core/talent/syle/enshroud_{}_icon.png",
        UNLOCK_LEVELS = [3, 7, 11, 15, 20, 24, 28, 32, 36, 40, 44, 50, 56, 62, 70, 76, 86, 98],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        CAST_TIME = 800,
        COOLDOWN = seconds(60),
        POWERS = [25, 25, 43, 43, 43, 55, 55, 55, 67, 67, 67, 74, 74, 74, 80, 80, 80, 90],
        SP_COSTS = [56, 52, 52, 52, 48, 48, 48, 44, 44, 44, 44, 40, 40, 40, 36, 36, 36, 36],
        TRIGGER_TIME = 900,
        BUFF_DURATIONS = [seconds(50), seconds(50), seconds(50), seconds(60), seconds(60), seconds(60), seconds(75), seconds(75), seconds(75), seconds(90), seconds(90), seconds(90), seconds(105), seconds(105), seconds(105), seconds(120), seconds(120), seconds(120)],
        POWER_UP_LEVEL = 5,
        POWER_UP_DURATION = minutes(1),
        POWER_UP_POTENCY = 0.4,
        TP_AMOUNT = 30,
        TP_CHANCE = 40,
        SOUND = "mods/core/audio/sfx/talent/syle/storm.ogg",
        SOUND_TIMING = 350
    )
    ENSHROUD_FORM_AEGNIX = AttrDict(NAME="Firestorm")
    ENSHROUD_FORM_AEOLUS = AttrDict(NAME="Windstorm")
    ENSHROUD_FORM_LACIES = AttrDict(NAME="Snowstorm")
    ENSHROUD_FORM_SILVAN = AttrDict(NAME="Sandstorm")

    #

    HASTE = AttrDict(
        NAME = "Haste",
        DESCRIPTION = "HasteDesc",
        ICON = "mods/core/talent/syle/haste_spell_icon.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 45, 51, 57, 63, 71, 77, 87, 99],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        CAST_TIME = 800,
        RANGE = 224,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 112, 112, 112, 112, 168, 168],
        SP_COSTS = [49, 46, 46, 46, 43, 43, 43, 40, 40, 40, 40, 40, 40, 40, 36, 36, 36, 36],
        SP_GAINS = [0, 0, 0, 0, 40, 40, 40, 70, 70, 70, 70, 70, 90, 90, 90, 90, 90, 110],
        BUFF_DURATIONS = [seconds(180), seconds(180), seconds(210), seconds(210), seconds(210), seconds(240), seconds(240), seconds(240), seconds(270), seconds(270), seconds(270), seconds(300), seconds(300), seconds(300), seconds(330), seconds(330), seconds(360), seconds(360)],
        COOLDOWN = seconds(30),
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        ATTACK_SPEEDS = [10, 10, 10, 14, 14, 14, 16, 16, 16, 20, 20, 20, 22, 22, 22, 24, 24, 25],
        SOUND_TIMING = 300,
        SOUND="mods/core/audio/sfx/talent/syle/haste.ogg"
    )

    #

    DISPEL = AttrDict(
        NAME = "Dispel",
        DESCRIPTION = "DispelDesc",
        ICON = "mods/core/talent/syle/dispel_spell_icon.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 44],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450],
        CAST_TIME = 800,
        RANGE = 112,
        SP_COSTS = [48, 44, 44, 40, 40, 40, 36, 36, 36, 32],
        SP_GAINS = [0, 0, 0, 0, 40, 40, 40, 80, 80, 80],
        BUFF_DURATION = minutes(4),
        COOLDOWNS = [seconds(40), seconds(40), seconds(35), seconds(35), seconds(35), seconds(30), seconds(30), seconds(30), seconds(25), seconds(25)],
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        SOUND_TIMING = 310,
        SOUND="mods/core/audio/sfx/talent/syle/dispel.ogg"
    )

    #

    VEIL = AttrDict(
        NAME = "Veil",
        DESCRIPTION = "VeilSpellDesc",
        ICON = "mods/core/talent/syle/veil_spell_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 49, 58, 67, 77, 88, 100],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 450, 500, 500, 500],
        CAST_TIME = 800,
        RANGE = 112,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112],
        SP_COSTS = [60, 56, 56, 56, 52, 52, 52, 48, 48, 48],
        SP_GAINS = [0, 0, 0, 0, 40, 40, 40, 80, 80, 80],
        BUFF_DURATION = minutes(2),
        COOLDOWNS = [seconds(90), seconds(90), seconds(75), seconds(75), seconds(75), seconds(60), seconds(60), seconds(60), seconds(45), seconds(45)],
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        VEIL_AMOUNTS = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
        SOUND_TIMING = 310,
        SOUND="mods/core/audio/sfx/talent/syle/veil.ogg"
    )

    #

    STONESKIN = AttrDict(
        NAME = "Stoneskin",
        DESCRIPTION = "StoneskinSpellDesc",
        ICON = "mods/core/talent/syle/stoneskin_spell_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 51, 63, 75, 87, 99],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 500, 500, 500, 550],
        CAST_TIME = 800,
        RANGE = 224,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 168, 168, 168],
        SP_COSTS = [60, 56, 56, 56, 52, 52, 52, 48, 48, 48, 45, 45, 45, 42, 42],
        SP_GAINS = [0, 0, 0, 0, 40, 40, 40, 80, 80, 80, 100, 100, 100, 120, 120],
        BUFF_DURATION = minutes(2),
        COOLDOWNS = [seconds(90), seconds(90), seconds(75), seconds(75), seconds(75), seconds(60), seconds(60), seconds(60), seconds(45), seconds(45), seconds(45), seconds(40), seconds(40), seconds(40), seconds(35)],
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        ABSORBED_AMOUNTS = [60, 60, 60, 120, 120, 120, 210, 210, 210, 300, 300, 300, 390, 390, 390],
        SOUND_TIMING = 310,
        SOUND="mods/core/audio/sfx/talent/syle/stoneskin.ogg"
    )

    #

    RAISE = AttrDict(
        NAME = "Raise",
        DESCRIPTION = "RaiseDesc",
        ICON = "mods/core/talent/syle/raise_spell_icon.png",
        UNLOCK_LEVELS = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 50, 64, 80, 100],
        LEVEL_COSTS = [375, 375, 375, 400, 400, 400, 400, 450, 450, 500, 600, 700, 850, 1000],
        CAST_TIME = seconds(2),
        RANGE = 112,
        SP_COSTS = [80, 80, 70, 70, 70, 60, 60, 60, 50, 50, 50, 45, 45, 45],
        SP_GAINS = [0, 0, 0, 0, 40, 40, 40, 80, 80, 80, 80, 100, 100, 100],
        DURATION = minutes(4),
        COOLDOWN = seconds(60),
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        HEALTH_PERCENTAGES = [20, 25, 25, 45, 45, 45, 65, 65, 65, 85, 85, 85, 100],
        SOUND_TIMING = 310,
        SOUND="mods/core/audio/sfx/talent/syle/dispel.ogg"
    )

    #

    REGENERATE = AttrDict(
        NAME = "Regenerate",
        DESCRIPTION = "RegenerateDesc",
        ICON = "mods/core/talent/syle/regenerate_spell_icon.png",
        UNLOCK_LEVELS = [3, 8, 12, 16, 20, 24, 28, 32, 36, 40, 50, 60, 75, 90],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 500, 600, 800, 1000],
        CAST_TIME = seconds(1),
        RANGE = 112,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 168, 168],
        SP_COST = 35,
        BUFF_DURATIONS = [seconds(20), seconds(23), seconds(23), seconds(23), seconds(26), seconds(26), seconds(26), seconds(30), seconds(30), seconds(30), seconds(35), seconds(35), seconds(35), seconds(40)],
        COOLDOWNS = [seconds(15), seconds(15), seconds(15), seconds(12), seconds(12), seconds(12), seconds(9), seconds(9), seconds(9), seconds(6), seconds(6), seconds(6), seconds(6), seconds(4)],
        TP_AMOUNT = 25,
        TP_CHANCE = 45,
        HEALTH_PERCENTAGES = [3, 3, 4, 4, 4, 5.5, 5.5, 5.5, 7, 7, 7, 7, 10, 10],
        SOUND = "mods/core/audio/sfx/talent/syle/regenerate.ogg",
        SOUND_TIMING = 300
    )

    #

    INVISIBLE = AttrDict(
        NAME = "Invisible",
        DESCRIPTION = "InvisibleDesc",
        ICON = "mods/core/talent/syle/invisible_spell_icon.png",
        UNLOCK_LEVELS = [10, 15, 20, 25, 30, 40, 55, 70, 85, 100],
        LEVEL_COSTS = [375, 400, 400, 450, 500, 550, 600, 650, 700, 750],
        CAST_TIME = seconds(1),
        RANGE = 224,
        AOE_RANGES = [0, 0, 0, 0, 0, 0, 112, 112, 112, 112, 112, 112, 168, 168, 168],
        SP_COST = 50,
        BUFF_DURATIONS = [seconds(120), seconds(150), seconds(150), seconds(180), seconds(180), seconds(180), seconds(210), seconds(210), seconds(210), seconds(240)],
        COOLDOWNS = [minutes(3), minutes(3), minutes(2), minutes(2), minutes(1), minutes(1), minutes(1), minutes(1), minutes(1), minutes(1)],
        TP_AMOUNT = 30,
        TP_CHANCE = 40,
        SOUND = "mods/core/audio/sfx/talent/syle/invisibility.ogg",
        SOUND_TIMING = 310
    )

    #

    BREATH_FORM = AttrDict(
        NAME = "BreathForm",
        TYPE = "Breath",
        DESCRIPTION = "BreathFormDesc",
        ICON = "mods/core/talent/syle/breath_icon.png",
        ICON_TEMPLATE = "mods/core/talent/syle/breath_{}_icon.png",
        UNLOCK_LEVELS = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 50, 58, 66, 76, 88],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 600, 600, 600, 600],
        CAST_TIME = 100,
        POWERS = [130, 133, 133, 139, 139, 139, 148, 148, 148, 160, 160, 160, 170, 170, 176],
        SP_COST = 15,
        SP_DRAINS = [12, 12, 10, 10, 10, 8, 8, 8, 6, 6, 6, 6, 6, 5, 5],
        COOLDOWN = seconds(2),
        POWER_UP_LEVEL = 10,
        POWER_UP_POTENCY = 0.55,
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        STATUS_EFFECT_CHANCES = [0, 0, 0, 0, 25, 25, 25, 40, 40, 40, 45, 45, 45, 50, 50],
        TRIGGER_TIME = 500,
    )
    BREATH_FORM_AEGNIX = AttrDict(NAME="Flamethrower", SOUND="mods/core/audio/sfx/talent/syle/haste.ogg", SOUND_TIMING=300)
    BREATH_FORM_LACIES = AttrDict(NAME="Avalanche", SOUND="mods/core/audio/sfx/talent/syle/dispel.ogg")
    BREATH_FORM_AEOLUS = AttrDict(NAME="Gust", SOUND="mods/core/audio/sfx/talent/syle/veil.ogg")
    BREATH_FORM_SILVAN = AttrDict(NAME="Earthfall", SOUND="mods/core/audio/sfx/talent/syle/stoneskin.ogg")

    #

    BEAM_FORM = AttrDict(
        NAME = "BeamForm",
        TYPE = "Beam",
        DESCRIPTION = "BeamFormDesc",
        ICON = "mods/core/talent/syle/beam_icon.png",
        ICON_TEMPLATE = "mods/core/talent/syle/beam_{}_icon.png",
        UNLOCK_LEVELS = [9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 51, 59, 67, 77, 89],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 600, 600, 600, 600],
        POWERS = [155, 155, 165, 165, 165, 185, 185, 185, 200, 200, 200, 215, 215, 215, 225],
        RANGE = 250,
        CAST_TIME = 800,
        SP_COST = 55,
        COOLDOWN = seconds(5),
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        BEAM_LENGTHS = [250, 250, 250, 300, 300, 300, 400, 400, 400, 400, 500, 500, 500, 500, 500],
        CHAIN_COUNTS = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    )
    BEAM_FORM_AEGNIX = AttrDict(NAME="Firebeam", SOUND="mods/core/audio/sfx/talent/syle/haste.ogg", SOUND_TIMING=300)
    BEAM_FORM_LACIES = AttrDict(NAME="Icebeam", SOUND="mods/core/audio/sfx/talent/syle/dispel.ogg")
    BEAM_FORM_AEOLUS = AttrDict(NAME="Windbeam", SOUND="mods/core/audio/sfx/talent/syle/veil.ogg")
    BEAM_FORM_SILVAN = AttrDict(NAME="Earthbeam", SOUND="mods/core/audio/sfx/talent/syle/stoneskin.ogg")

    #

    BLAST_FORM = AttrDict(
        NAME = "BlastForm",
        TYPE = "Blast",
        DESCRIPTION = "BlastFormDesc",
        ICON = "mods/core/talent/syle/blast_icon.png",
        ICON_TEMPLATE = "mods/core/talent/syle/blast_{}_icon.png",
        UNLOCK_LEVELS = [10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 52, 60, 68, 78, 90],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 600, 600, 600, 600],
        CAST_TIME = seconds(1),
        POWERS = [170, 170, 180, 180, 180, 195, 195, 195, 210, 210, 210, 225, 225, 225, 235],
        STUN_TIMES = [0, 0, 0, 0, seconds(1), seconds(1), seconds(1), seconds(2), seconds(2), seconds(2), seconds(3), seconds(3), seconds(4), seconds(4), seconds(5)],
        SP_COSTS = [57, 53, 53, 49, 49, 49, 45, 45, 45, 41, 41, 41, 36, 36, 36],
        COOLDOWN = seconds(5),
        TP_AMOUNT = 20,
        TP_CHANCE = 30,
        ERUPTION_POWER = 45,
        ERUPTION_LIFETIME = seconds(5),
    )
    BLAST_FORM_AEGNIX = AttrDict(NAME="Blaze", SOUND="mods/core/audio/sfx/talent/syle/haste.ogg", SOUND_TIMING=300)
    BLAST_FORM_LACIES = AttrDict(NAME="Torrent", SOUND="mods/core/audio/sfx/talent/syle/dispel.ogg")
    BLAST_FORM_AEOLUS = AttrDict(NAME="Gale", SOUND="mods/core/audio/sfx/talent/syle/veil.ogg")
    BLAST_FORM_SILVAN = AttrDict(NAME="Quake", SOUND="mods/core/audio/sfx/talent/syle/stoneskin.ogg")

    #

    # Arms Skills
    AGILITY_BOOST = AttrDict(
        NAME = "AgilityBoost",
        DESCRIPTION = "AgilityBoostDesc",
        ICON = "mods/core/talent/arms/agility_boost_icon.png",
        UNLOCK_LEVELS = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 69, 75, 81, 88, 95, 100],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 700, 700, 800, 800, 900, 900, 900, 1000],
        STAT = 'AGI',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 74, 80]
    )
    #
    ATTACK_BOOST = AttrDict(
        NAME = "AttackBoost",
        DESCRIPTION = "AttackBoostDesc",
        ICON = "mods/core/talent/arms/attack_boost_icon.png",
        UNLOCK_LEVELS = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 69, 75, 81, 88, 95, 100],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 700, 700, 800, 800, 900, 900, 900, 1000],
        STAT = 'ATK',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 74, 80]
    )
    #
    DEFENSE_BOOST = AttrDict(
        NAME = "DefenseBoost",
        DESCRIPTION = "DefenseBoostDesc",
        ICON = "mods/core/talent/arms/defense_boost_icon.png",
        UNLOCK_LEVELS = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 69, 75, 81, 88, 95, 100],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 600, 700, 700, 800, 800, 900, 900, 900, 1000],
        STAT = 'DEF',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 74, 80]
    )
    #
    SWORD_PROFICIENCY = AttrDict(
        NAME = "SwordProficiency",
        DESCRIPTION = "SwordProficiencyDesc",
        ICON = "mods/core/talent/arms/sword_proficiency_icon.png",
        UNLOCK_LEVELS = [1, 7, 14, 22, 30],
        LEVEL_COSTS = [100, 450, 500, 600, 700],
    )
    SPEAR_PROFICIENCY = AttrDict(
        NAME = "SpearProficiency",
        DESCRIPTION = "SpearProficiencyDesc",
        ICON = "mods/core/talent/arms/spear_proficiency_icon.png",
        UNLOCK_LEVELS = [1, 7, 14, 22, 30],
        LEVEL_COSTS = [400, 450, 500, 600, 700],
    )
    BOW_PROFICIENCY = AttrDict(
        NAME = "BowProficiency",
        DESCRIPTION = "BowProficiencyDesc",
        ICON = "mods/core/talent/arms/bow_proficiency_icon.png",
        UNLOCK_LEVELS = [1, 7, 14, 22, 30],
        LEVEL_COSTS = [400, 450, 500, 600, 700],
    )
    SHIELD_PROFICIENCY = AttrDict(
        NAME = "ShieldProficiency",
        DESCRIPTION = "ShieldProficiencyDesc",
        ICON = "mods/core/talent/arms/shield_proficiency_icon.png",
        UNLOCK_LEVELS = [1, 7, 14, 22, 30],
        LEVEL_COSTS = [400, 450, 500, 600, 700],
    )

    FOCUS = AttrDict(
        NAME = "Focus",
        DESCRIPTION = "FocusDesc",
        ICON = "mods/core/talent/arms/focus_skill_icon.png",
        UNLOCK_LEVELS = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 43, 50, 57, 65, 73, 81, 89, 97],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        CAST_TIME = 800,
        CRITICAL_MODIFIERS = [0, 20, 20, 50, 50, 50, 100, 100, 100, 150, 150, 150, 200, 200, 200, 200, 250, 250],
        COOLDOWNS = [seconds(20), seconds(20), seconds(17), seconds(17), seconds(17), seconds(14), seconds(14), seconds(14), seconds(11), seconds(11), seconds(11), seconds(9), seconds(9), seconds(9), seconds(8), seconds(8), seconds(8)],
        SP_COSTS = [40, 35, 35, 35, 30, 30, 30, 25, 25, 25, 25, 20, 20, 20, 20, 15, 15, 15],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        SOUND = "mods/core/audio/sfx/talent/arms/focus.ogg",
    )

    BATTLE_CRY = AttrDict(
        NAME = "BattleCry",
        DESCRIPTION = "BattleCryDesc",
        ICON = "mods/core/talent/arms/battle_cry_skill_icon.png",
        UNLOCK_LEVELS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 46, 53, 60, 68, 76, 84, 92, 100],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        CAST_TIME = 800,
        RANGE = 112,
        COOLDOWN = seconds(30),
        STAT_BUFFS = [10, 10, 10, 20, 20, 20, 30, 30, 30, 40, 40, 40, 50, 50, 50, 60, 60, 75],
        SP_COSTS = [55, 50, 50, 50, 45, 45, 45, 40, 40, 40, 40, 35, 35, 35, 35, 30, 30, 30],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        BUFF_DURATIONS = [seconds(180), seconds(180), seconds(210), seconds(210), seconds(210), seconds(240), seconds(240), seconds(240), seconds(270), seconds(270), seconds(270), seconds(300), seconds(300), seconds(300), seconds(330), seconds(330), seconds(330), seconds(360)],
        SOUND = "mods/core/audio/sfx/talent/arms/battle_cry.ogg",
    )
    #

    BERSERK = AttrDict(
        NAME = "Berserk",
        DESCRIPTION = "BerserkDesc",
        ICON = "mods/core/talent/arms/berserk_skill_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 47, 54, 61, 68, 75, 82, 89, 96],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        CAST_TIME = 600,
        STAT_BUFFS = [40, 40, 40, 80, 80, 80, 120, 120, 120, 160, 160, 160, 200, 200, 200, 240, 240, 240],
        COOLDOWNS = [seconds(60), seconds(60), seconds(40), seconds(40), seconds(40), seconds(20), seconds(20), seconds(20), seconds(1), seconds(1), seconds(1), seconds(1), seconds(1), seconds(1), seconds(1), seconds(1), seconds(1), seconds(1)],
        SP_COST = 10,
        SP_DRAINS = [10, 9, 9, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        SOUND = "mods/core/audio/sfx/talent/arms/berserker_heartbeat1.ogg",
    )
    #
    STUN = AttrDict(
        NAME = "Stun",
        DESCRIPTION = "StunDesc",
        ICON = "mods/core/talent/arms/stun_skill_icon.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 44, 50, 56, 62, 68, 74, 80, 86, 92],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        COOLDOWNS = [seconds(20), seconds(20), seconds(17), seconds(17), seconds(17), seconds(14), seconds(14), seconds(14), seconds(11), seconds(11), seconds(11), seconds(9), seconds(9), seconds(9), seconds(8), seconds(8), seconds(8), seconds(7)],
        STUN_TIMES = [seconds(1), seconds(1), seconds(1), seconds(2), seconds(2), seconds(2), seconds(3), seconds(3), seconds(3), seconds(4), seconds(4), seconds(4), seconds(5), seconds(5), seconds(5), seconds(6), seconds(6), seconds(6)],
        SP_COSTS = [42, 38, 38, 38, 34, 34, 34, 30, 30, 30, 26, 26, 26, 22, 22, 22, 18, 18],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
    )
    #
    KNOCKBACK = AttrDict(
        NAME = "Knockback",
        DESCRIPTION = "KnockbackDesc",
        ICON = "mods/core/talent/arms/knockback_skill_icon.png",
        UNLOCK_LEVELS = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 47, 53, 59, 65, 71, 77, 83],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        COOLDOWNS = [seconds(20), seconds(20), seconds(17), seconds(17), seconds(17), seconds(14), seconds(14), seconds(14), seconds(11), seconds(11), seconds(11), seconds(9), seconds(9), seconds(9), seconds(8), seconds(8), seconds(8), seconds(7)],
        POWERS = [120, 120, 120, 135, 130, 130, 160, 160, 160, 180, 180, 180, 200, 200, 200, 220, 220, 220],
        SP_COSTS = [44, 41, 41, 41, 38, 38, 38, 35, 35, 35, 32, 32, 32, 30, 30, 30, 28, 28],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        KNOCKBACK = 12,
    )
    #
    ENSNARE = AttrDict(
        NAME = "Ensnare",
        DESCRIPTION = "EnsnareDesc",
        ICON = "mods/core/talent/arms/ensnare_skill_icon.png",
        UNLOCK_LEVELS = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 47, 53, 59, 65, 71, 77, 83],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        COOLDOWNS = [seconds(25), seconds(22), seconds(22), seconds(22), seconds(19), seconds(19), seconds(19), seconds(15), seconds(15), seconds(15), seconds(12), seconds(12), seconds(12), seconds(10), seconds(10), seconds(10), seconds(8), seconds(8)],
        POWERS = [120, 120, 120, 126, 126, 126, 134, 134, 134, 145, 145, 145, 152, 152, 152, 155, 155, 155],
        SNARE_TIMES = [seconds(3), seconds(3), seconds(4), seconds(4), seconds(4), seconds(6), seconds(6), seconds(6), seconds(8), seconds(8), seconds(8), seconds(9), seconds(9), seconds(9), seconds(10), seconds(10), seconds(10), seconds(12)],
        SP_COST = 35,
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
    )
    #
    SKY_SWORD = AttrDict(
        NAME = "SkySword",
        DESCRIPTION = "SkySwordDesc",
        ICON = "mods/core/talent/arms/sky_sword_skill_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 45, 50, 56, 62, 68, 74, 80],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        COOLDOWNS = [seconds(25), seconds(25), seconds(20), seconds(20), seconds(20), seconds(15), seconds(15), seconds(15), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10)],
        POWERS = [135, 135, 135, 150, 150, 150, 170, 170, 170, 195, 195, 195, 210, 210, 210, 220, 220, 220],
        SP_COSTS = [50, 46, 46, 46, 42, 42, 42, 38, 38, 38, 36, 36, 36, 34, 34, 34, 32, 32],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        DAMAGE_BOUNCE_MULTIPLER = 110,
        SOUND = "mods/core/audio/sfx/talent/arms/sky_form_fall.ogg",
    )
    #
    SLAM = AttrDict(
        NAME = "Slam",
        DESCRIPTION = "SlamDesc",
        ICON = "mods/core/talent/arms/slam_skill_icon.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 44, 49, 55, 61, 67, 73, 79],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        COOLDOWNS = [seconds(25), seconds(25), seconds(20), seconds(20), seconds(20), seconds(15), seconds(15), seconds(15), seconds(10), seconds(10)],
        POWERS = [115, 115, 115, 122, 122, 122, 130, 130, 130, 140, 140, 140, 150, 150, 150, 156, 156, 156],
        STUN_TIMES = [seconds(1), seconds(1.5), seconds(1.5), seconds(1.5), seconds(2), seconds(2), seconds(2), seconds(2.5), seconds(2.5), seconds(2.5), seconds(3), seconds(3), seconds(3), seconds(3.5), seconds(3.5), seconds(3.5), seconds(4), seconds(5)],
        SP_COST = 45,
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        SOUND = "mods/core/audio/sfx/talent/arms/sky_form_fall.ogg",
    )
    #
    DASH = AttrDict(
        NAME = "Dash",
        DESCRIPTION = "DashDesc",
        ICON = "mods/core/talent/arms/dash_skill_icon.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 44, 49, 55, 61, 67, 73, 79],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        POWERS = [0, 100, 100, 110, 110, 120, 130, 130, 140, 150],
        STUN_TIMES = [0, 0, 0, 0, seconds(.5), seconds(.8), seconds(.8), seconds(1.2), seconds(1.2), seconds(1.7)],
        COOLDOWNS = [seconds(30), seconds(30), seconds(20), seconds(15), seconds(15), seconds(15), seconds(15), seconds(15), seconds(15), seconds(15)],
        SP_COST = 35,
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
    )
    #
    TRIPLE_STRIKE = AttrDict(
        NAME = "TripleStrike",
        DESCRIPTION = "TripleStrikeDesc",
        ICON = "mods/core/talent/arms/triple_strike_skill_icon.png",
        UNLOCK_LEVELS = [9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 52, 58, 64, 70, 76, 83, 90, 97],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        RANGES = [180, 240, 240, 240, 300, 300, 300, 360, 360, 360, 400, 400, 400, 440, 440, 440, 460, 460],
        CAST_TIME = 900,
        COOLDOWNS = [seconds(25), seconds(25), seconds(20), seconds(20), seconds(20), seconds(15), seconds(15), seconds(15), seconds(10), seconds(10), seconds(10), seconds(8), seconds(8), seconds(8), seconds(7), seconds(7), seconds(7), seconds(6)],
        POWERS = [145, 145, 145, 160, 160, 160, 180, 180, 180, 200, 200, 200, 220, 220, 220, 240, 240, 240, 250],
        SP_COST = 48,
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
    )
    #
    SPIRIT_ARROW = AttrDict(
        NAME = "SpiritArrow",
        DESCRIPTION = "SpiritArrowDesc",
        ICON = "mods/core/talent/arms/spirit_arrow_skill_icon.png",
        UNLOCK_LEVELS = [10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 53, 59, 65, 71, 77, 84, 91, 98],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        RANGES = [180, 240, 240, 240, 300, 300, 300, 360, 360, 360, 400, 400, 400, 440, 440, 440, 460, 460],
        CAST_TIME = 900,
        COOLDOWNS = [seconds(25), seconds(25), seconds(20), seconds(20), seconds(20), seconds(15), seconds(15), seconds(15), seconds(10), seconds(10), seconds(10), seconds(9), seconds(9), seconds(9), seconds(8), seconds(8), seconds(8), seconds(7)],
        POWERS = [130, 130, 130, 142, 142, 142, 160, 160, 160, 180, 180, 180, 200, 200, 200, 210, 215, 220],
        SP_COST = 49,
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
    )
    #
    WALLER = AttrDict(
        NAME = "Waller",
        DESCRIPTION = "WallerDesc",
        ICON = "mods/core/talent/arms/waller_skill_icon.png",
        UNLOCK_LEVELS = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 50, 56, 62, 68, 74, 80, 87, 94],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450, 450, 450, 500, 500, 500, 550, 550, 600],
        RANGE = 192,
        CAST_TIME = 900,
        COOLDOWNS = [seconds(25), seconds(20), seconds(20), seconds(20), seconds(15), seconds(15), seconds(15), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10), seconds(10)],
        WALL_CREATE_TIME = 45,
        WALL_HEIGHTS = [5, 5, 5, 6, 6, 6, 8, 8, 8, 10, 10, 10, 12, 12, 12, 14, 14, 15],
        WALL_LIFETIMES = [seconds(2.5), seconds(2.5), seconds(3), seconds(3), seconds(3), seconds(3.5), seconds(3.5), seconds(3.5), seconds(4), seconds(4), seconds(4), seconds(4.5), seconds(4.5), seconds(4.5), seconds(5), seconds(5), seconds(5), seconds(5)],
        SP_COST = 35,
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
    )
    #
    # Craft Skills
    EXPERTISE = AttrDict(
        NAME = "Expertise",
        DESCRIPTION = "ExpertiseDesc",
        ICON = "mods/core/talent/craft/expertise.png",
        UNLOCK_LEVELS = [1, 3, 7, 11, 15, 19, 23, 27, 31, 35, 45, 55, 65, 75, 85, 95],
        LEVEL_COSTS = [100, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900],
        UP_QUALITY_MAXIMUMS = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400],
    )
    #
    REFINE = AttrDict(
        NAME = "Refine",
        DESCRIPTION = "RefineDesc",
        ICON = "mods/core/talent/craft/refine.png",
        UNLOCK_LEVELS = [1, 7, 15, 23, 31, 50, 60, 70, 80, 90, 100],
        LEVEL_COSTS = [0, 1000, 2000, 3000, 4000, 4200, 4400, 4600, 4800, 5000, 5000],
        STEP_COST = 1,
        QUALITY_AMOUNTS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    )
    #
    POLISH = AttrDict(
        NAME = "Polish",
        DESCRIPTION = "PolishDesc",
        ICON = "mods/core/talent/craft/polish.png",
        UNLOCK_LEVELS = [2, 8, 17, 26, 35, 46, 57, 68, 79, 90],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
        STEP_COST = 3,
        DURATIONS = [6, 8, 8, 8, 10, 10, 10, 12, 12, 12],
        RECHARGES = [9, 9, 5, 5, 5, 4, 4, 4, 3, 3],
        QUALITY_AMOUNTS = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
    )
    #
    INNOVATE = AttrDict(
        NAME = "Innovate",
        DESCRIPTION = "InnovateDesc",
        ICON = "mods/core/talent/craft/innovate.png",
        UNLOCK_LEVELS = [3, 9, 18, 27, 36, 50, 65, 80, 95],
        LEVEL_COSTS = [400, 500, 600, 700, 800, 900, 1000, 1100, 1200],
        RESEARCH_LEVELS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    #
    # SCRAP_MASTER = AttrDict(
    #    NAME = "ScrapMaster",
    #    DESCRIPTION = "ScrapMasterDesc",
    #    ICON = "mods/core/talent/craft/scrap_master.png",
    #    UNLOCK_LEVELS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],
    #    LEVEL_COSTS = [400, 500, 600, 650, 700, 750, 800, 850, 900, 950],
    #    BONUS_CHANCES = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # )

    # # st.SCRAP_MASTER = SCRAP_MASTER
    # Did not modify
    COMBAT_CHAOS = AttrDict(
        NAME = "CombatChaos",
        DESCRIPTION = "CombatChaosDesc",
        ICON = "mods/core/talent/craft/combat_chaos.png",
        UNLOCK_LEVELS = [3, 10, 19, 28, 37, 57, 72, 87],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1100, 1200],
        STEP_COST = 2,
        DURATIONS = [3, 5, 5, 5, 7, 7, 7, 9],
        RECHARGES = [20, 20, 10, 10, 10, 8, 8, 8],
        CHAOS_CHANGES = [-2, -2, -2, -4, -4, -4, -6, -6]
    )
    #
    SHARPEN = AttrDict(
        NAME = "Sharpen",
        DESCRIPTION = "SharpenDesc",
        ICON = "mods/core/talent/craft/sharpen.png",
        UNLOCK_LEVELS = [4, 11, 19, 27, 35, 55, 70, 85],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1100, 1200],
        STEP_COST = 4,
        DURATIONS = [6, 8, 8, 8, 10, 10, 10, 12],
        RECHARGES = [8, 8, 8, 4, 4, 3, 3, 3],
        QUALITY_AMOUNTS = [2, 2, 4, 4, 4, 6, 6, 6]
    )
    #
    CATALYST_RESEARCH = AttrDict(
        NAME = "CatalystResearch",
        DESCRIPTION = "CatalystResearchDesc",
        ICON = "mods/core/talent/craft/catalyst_research.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 60, 75, 90],
        LEVEL_COSTS = [350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950],
        BONUS_CATALYSTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    )
    #
    MODIFY_CATALYST = AttrDict(
        NAME = "ModifyCatalyst",
        DESCRIPTION = "ModifyCatalystDesc",
        ICON = "mods/core/talent/craft/modify_cataly# st.png",
        UNLOCK_LEVELS = [2, 10, 18, 26, 34, 54, 74, 94],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1100, 1200],
        STEP_COSTS = [3, 3, 2, 2, 2, 1, 1, 1],
        DURATIONS = [1, 2, 2, 3, 4, 4, 5, 6],
        CHAOS_CHANGE = -5
    )
    #
    MAGNIFY = AttrDict(
        NAME = "Magnify",
        DESCRIPTION = "MagnifyDesc",
        ICON = "mods/core/talent/craft/magnify.png",
        UNLOCK_LEVELS = [5, 13, 21, 29, 37, 58, 73, 88],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1100, 1200],
        STEP_COSTS = [3, 3, 2, 2, 2, 1, 1, 1],
        DURATIONS = [2, 3, 3, 3, 3, 4, 4, 4, 5],
        RECHARGES = [25, 25, 25, 20, 20, 20, 15, 15],
    )
    # st.MAGNIFY = MAGNIFY
    # CONVERT_CHAOS = AttrDict(
    #    NAME = "ConvertChaos",
    #    DESCRIPTION = "ConvertChaosDesc",
    #    ICON = "mods/core/talent/craft/convert_chaos.png",
    #    UNLOCK_LEVELS = [6, 14, 22, 30, 38],
    #    LEVEL_COSTS = [500, 600, 700, 800, 900],
    #    STEP_COST = 3,
    #    DURATIONS = [2, 2, 3, 3, 3],
    #    RECHARGES = [20, 20, 20, 15, 15],
    #    CONVERSION_AMOUNTS = [50, 75, 75, 75, 100]
    # )
    # POSTPONE = AttrDict(
    #    NAME = "Postpone",
    #    DESCRIPTION = "PostponeDesc",
    #    ICON = "mods/core/talent/craft/postpone.png",
    #    UNLOCK_LEVELS = [8, 20, 32],
    #    LEVEL_COSTS = [500, 700, 900],
    #    STEP_COSTS = [3, 2, 1],
    #    DURATION = 'CT',
    #    CHAOS_CHANGE = 8
    # )
    # RECOURSE = AttrDict(
    #    NAME = "Recourse",
    #    DESCRIPTION = "RecourseDesc",
    #    ICON = "mods/core/talent/craft/recourse.png",
    #    UNLOCK_LEVELS = [20],
    #    LEVEL_COSTS = [1000],
    #    STEP_COST = 2,
    #    RECHARGE = 3,
    # )
    # DELAY = AttrDict(
    #    NAME = "Delay",
    #    DESCRIPTION = "DelayDesc",
    #    ICON = "mods/core/talent/craft/delay.png",
    #    UNLOCK_LEVELS = [21],
    #    LEVEL_COSTS = [1000],
    #    STEP_COST = 2,
    #    DURATION = 5,
    #    RECHARGE = 2,
    #    STEP_CHANGE = 3
    # )
    MATERIAL_MASTER = AttrDict(
        NAME = "MaterialMaster",
        DESCRIPTION = "MaterialMasterDesc",
        ICON = "mods/core/talent/craft/material_master.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 44, 50, 54, 60, 66, 72, 78, 85, 92],
        LEVEL_COSTS = [300, 350, 400, 400, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
        BONUS_QUALITYS = [4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 26, 28, 30, 32, 34, 36, 38]
    )
    #

    # Gather Skills
    TOOL_PROFICIENCY = AttrDict(
        NAME = "ToolProficiency",
        DESCRIPTION = "ToolProficiencyDesc",
        ICON = "mods/core/talent/gather/use_tool_1_icon.png",
        UNLOCK_LEVELS = [1, 3, 8, 17, 30, 50, 75, 100],
        LEVEL_COSTS = [100, 500, 700, 900, 1100, 1200, 1300, 1500],
        MAX_TOOL_STATE = [1, 1, 2, 2, 2, 2, 2, 2],
        STATE_TILE_RADIUS = [1, 2, 3],
        STATE_MULTIPLIERS = [
            [1, 1, 1, 1, 1.5, 1.5, 1.5, 1.5],
            [0.6, 1, 1, 1, 1, 1.5, 1.5, 1.5],
            [0, 0, 0.6, 1, 1, 1, 1, 1.5]
        ],
        DOUBLE_MULTIPLIERS = [60, 100, 100, 100, 100, 100, 100, 100],
        TRIPLE_MULTIPLIERS = [60, 60, 60, 100, 100, 100, 100, 100],
    )
    #
    HEALTH_BOOST = AttrDict(
        NAME = "HealthBoost",
        DESCRIPTION = "HealthBoostDesc",
        ICON = "mods/core/talent/explore/stamina_boost_icon.png",
        UNLOCK_LEVELS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200],
        STAT = 'HP',
        STAT_AMOUNTS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 220, 250]
    )
    #
    TOOL_SPEED = AttrDict(
        NAME = "ToolSpeed",
        DESCRIPTION = "ToolSpeedDesc",
        ICON = "mods/core/talent/gather/tool_speed_boost_icon.png",
        UNLOCK_LEVELS = [4, 8, 13, 18, 23, 27, 32, 36, 40, 44, 50, 56, 64, 72, 80, 90, 100],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950],
        STAT_AMOUNTS = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 32, 34, 36, 38, 40, 42, 45]
    )
    #
    TOOL_POWER = AttrDict(
        NAME = "ToolPower",
        DESCRIPTION = "ToolPowerDesc",
        ICON = "mods/core/talent/gather/tool_power_boost_icon.png",
        UNLOCK_LEVELS = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 47, 53, 68, 76, 85, 95],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950],
        STAT_AMOUNTS = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 32, 34, 36, 38, 40, 42, 45]
    )
    #
    TOOL_REACH = AttrDict(
        NAME = "ToolReach",
        DESCRIPTION = "ToolReachDesc",
        ICON = "mods/core/talent/gather/tool_reach_boost_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 50, 60, 70, 85, 100],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 700, 800, 900, 1000, 1200],
        STAT = 'reach',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
    )
    #
    PICKUP_REACH = AttrDict(
        NAME = "PickupReach",
        DESCRIPTION = "PickupReachDesc",
        ICON = "mods/core/talent/gather/pickup_reach_boost_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 50, 60, 70, 85, 100],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 700, 800, 900, 1000, 1200],
        STAT = 'pickup',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
    )
    #
    RESOURCEFUL = AttrDict(
        NAME = "ResourcefulGatherer",
        DESCRIPTION = "ResourcefulGathererDesc",
        ICON = "mods/core/talent/gather/resourceful_icon.png",
        UNLOCK_LEVELS = [5, 13, 21, 29, 37, 50, 60, 70, 80, 90],
        LEVEL_COSTS = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250],
        ITEM_CHANCES = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    )
    #
    BARTER = AttrDict(
        NAME = "Barter",
        DESCRIPTION = "BarterDesc",
        ICON = "mods/core/talent/gather/barter_icon.png",
        UNLOCK_LEVELS = [8, 16, 24, 32, 40, 50, 75, 100],
        LEVEL_COSTS = [600, 700, 800, 900, 1000, 1200, 1400, 1600],
        DISCOUNT_AMOUNTS = [5, 10, 15, 20, 25, 30, 35, 40]
    )
    #
    SCAVENGE = AttrDict(
        NAME = "Scavenge",
        DESCRIPTION = "ScavengeDesc",
        ICON = "mods/core/talent/gather/scavenge_icon.png",
        UNLOCK_LEVELS = [5, 13, 21, 29, 37, 50, 75],
        LEVEL_COSTS = [400, 600, 800, 1000, 1200, 1400, 1600],
        SCRAP_CHANCE = 5,
        ORES = ['copper_ore', 'iron_ore', 'silver_ore', 'gold', 'adamantite', 'corium', 'osmium'],
    )
    #
    ORE_HUNTER = AttrDict(
        NAME = "OreHunter",
        DESCRIPTION = "OreHunterDesc",
        ICON = "mods/core/talent/gather/ore_hunter_icon.png",
        CAST_TIME = 1500,
        UNLOCK_LEVELS = [3, 6, 11, 14, 23, 31, 38],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1000],
        COOLDOWN = seconds(60),
        ORES = ['copper_ore', 'iron_ore', 'silver_ore', 'gold', 'adamantite', 'corium', 'osmium'],
        DURATION = seconds(12)
    )
    # #
    INCREASE_DROP_RATE = AttrDict(
        NAME = "IncreaseDropRate",
        DESCRIPTION = "IncreaseDropRateDesc",
        ICON = "mods/core/talent/gather/increase_drop_rate_icon.png",
        UNLOCK_LEVELS = [10, 18, 26, 34, 42],
        LEVEL_COSTS = [600, 700, 800, 900, 1000],
        AMOUNTS = [20, 40, 60, 80, 100]
    )
    # #
    PRECISION = AttrDict(
        NAME = "Precision",
        DESCRIPTION = "PrecisionDesc",
        ICON = "mods/core/talent/gather/precision_icon.png",
        UNLOCK_LEVELS = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 50, 56, 63, 70, 78, 86, 94],
        LEVEL_COSTS = [500, 600, 700, 800, 900, 1000, 1000, 1000, 1000, 1000, 1100, 1100, 1200, 1200, 1300, 1400, 1500],
        CHANCES = [10, 10, 10, 15, 15, 15, 20, 20, 20, 25, 25, 25, 30, 30, 30, 35, 35],
        CAST_TIME = 500,
        COOLDOWNS = [seconds(180), seconds(165), seconds(165), seconds(165), seconds(150), seconds(150), seconds(150), seconds(135), seconds(135), seconds(120), seconds(120), seconds(110), seconds(110), seconds(105), seconds(105), seconds(100), seconds(100)],
        BUFF_DURATIONS = [seconds(60), seconds(60), seconds(75), seconds(75), seconds(75), seconds(90), seconds(90), seconds(90), seconds(120), seconds(120), seconds(150), seconds(150), seconds(180), seconds(180), seconds(210), seconds(210), seconds(240)]
    )
    #

    # Explore Skills
    LEDGE_GRAB = AttrDict(
        NAME = "LedgeGrab",
        DESCRIPTION = "LedgeGrabDesc",
        ICON = "mods/core/talent/explore/ledge_grab_icon.png",
        UNLOCK_LEVELS = [1],
        LEVEL_COSTS = [500]
    )
    SHADOW_FOLDING = AttrDict(
        NAME = "ShadowFolding",
        DESCRIPTION = "ShadowFoldingDesc",
        ICON = "mods/core/talent/explore/shadow_folding_icon.png",
        UNLOCK_LEVELS = [1, 3, 10, 20, 30],
        LEVEL_COSTS = [0, 1000, 1000, 1000, 1000],
        CAPACITY = [1, 2, 3, 4, 5],
        INITIAL_BAG_SIZE = 25
    )
    STAMINA_BOOST = AttrDict(
        NAME = "StaminaBoost",
        DESCRIPTION = "StaminaBoostDesc",
        ICON = "mods/core/talent/explore/stamina_boost_icon.png",
        UNLOCK_LEVELS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 60, 65, 70, 76, 84, 92],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200],
        STAT = 'SP',
        STAT_AMOUNTS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]
    )
    #
    TREASURE_HUNTER = AttrDict(
        NAME = "TreasureHunter",
        DESCRIPTION = "TreasureHunterDesc",
        ICON = "mods/core/talent/explore/treasure_hunter_icon.png",
        CAST_TIME = 1500,
        UNLOCK_LEVELS = [2, 7, 14, 24],
        LEVEL_COSTS = [800, 900, 950, 1000],
        COOLDOWN = seconds(60),
        # Later modify with a new chest type
        TREASURE_CHESTS = ['wooden', 'silver', 'gold', 'alatrian'],
        DURATION = seconds(12)
    )
    # #
    LUCK_BOOST = AttrDict(
        NAME = "LuckBoost",
        DESCRIPTION = "LuckBoostDesc",
        ICON = "mods/core/talent/explore/luck_boost_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 58, 64, 70, 76, 82, 90, 98],
        LEVEL_COSTS = [375, 400, 400, 400, 400, 450, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200],
        STAT = 'LUCK',
        STAT_AMOUNTS = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    )
    #
    SPRINT = AttrDict(
        NAME = "Sprint",
        DESCRIPTION = "SprintDesc",
        ICON = "mods/core/talent/explore/sprint_icon.png",
        UNLOCK_LEVELS = [3, 14, 25, 60],
        LEVEL_COSTS = [1500, 1000, 500, 2500],
        SPEED = 4.3,
        SP_COSTS = [20, 0, 0, 0],
        SP_DRAINS = [2, 2, 1, 0]
    )
    #
    JUMP_HEIGHT = AttrDict(
        NAME = "JumpHeight",
        DESCRIPTION = "JumpHeightDesc",
        ICON = "mods/core/talent/explore/jump_height_icon.png",
        UNLOCK_LEVELS = [3, 9, 15, 21, 50, 79, 100],
        LEVEL_COSTS = [700, 800, 900, 1000, 1100, 1200, 1300],
        SPEED_PER_LEVEL = 0.2,
        JUMP_TIMES = [20, 40, 60, 80, 100, 120, 140]
    )
    #
    DODGE_EXPERTISE = AttrDict(
        NAME = "DodgeExpertise",
        DESCRIPTION = "DodgeExpertiseDesc",
        ICON = "mods/core/talent/explore/dodge_expertise_icon.png",
        UNLOCK_LEVELS = [3, 8, 14, 19, 24, 45, 66, 87],
        LEVEL_COSTS = [600, 700, 800, 900, 1000, 1100, 1200, 1300],
        SP_COST_REDUCTIONS = [5, 10, 15, 20, 25, 30, 35, 40]
    )
    #
    CARTOGRAPHY = AttrDict(
        NAME = "Cartography",
        DESCRIPTION = "CartographyDesc",
        ICON = "mods/core/talent/explore/cartography_icon.png",
        UNLOCK_LEVELS = [4, 8, 12, 16, 20, 40, 60, 80, 100],
        LEVEL_COSTS = [600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
        STAT = 'vision',
        STAT_AMOUNTS = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    )
    #
    LOCKPICK = AttrDict(
        NAME = "Lockpick",
        DESCRIPTION = "LockpickDesc",
        ICON = "mods/core/talent/explore/lockpick_icon.png",
        UNLOCK_LEVELS = [6, 12, 18, 24, 30, 50, 75, 100],
        LEVEL_COSTS = [600, 700, 800, 900, 1000, 1200, 1400, 1600],
        UNLOCK_CHANCES = [0, 10, 10, 20, 30, 40, 45, 50],
        TREASURE_CHESTS = ['silver', '', 'gold', '', 'alatrian'],
        INITIAL_CHEST_CHANCES = {
            'silver': 30,
            'gold': 20,
            'alatrian': 0
        }
    )
    #
    FLARE = AttrDict(
        NAME = "Flare",
        DESCRIPTION = "FlareDesc",
        ICON = "mods/core/talent/explore/flare_icon.png",
        UNLOCK_LEVELS = [3, 10, 17, 24, 31, 40, 50, 61, 73, 85],
        LEVEL_COSTS = [600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],
        COOLDOWNS = [seconds(90), seconds(75), seconds(75), seconds(60), seconds(60), seconds(45), seconds(45), seconds(35), seconds(35), seconds(30)],
        TRAVEL_TIMES = [seconds(0.5), seconds(1), seconds(1.5), seconds(2), seconds(2.5), seconds(3), seconds(3.5), seconds(4), seconds(4.5), seconds(5)]
    )

    DOUBLE_JUMP = AttrDict(
        NAME = "DoubleJump",
        DESCRIPTION = "DoubleJumpDesc",
        ICON = "mods/core/talent/explore/double_jump_icon.png",
        UNLOCK_LEVELS = [5],
        LEVEL_COSTS = [2000]
    )
    FEATHER_FALLING = AttrDict(
        NAME = "FeatherFall",
        DESCRIPTION = "FeatherFallDesc",
        ICON = "mods/raisecap/talent/explore/feather_fall_icon.png",
        UNLOCK_LEVELS = [40, 60, 80, 100],
        LEVEL_COSTS = [1000, 1100, 1200, 1300],
        FALL_REDUCTIONS = [10, 20, 30, 40]
    )
    CRYSTAL_DOWSING = AttrDict(
        NAME = "CrystalDowsing",
        DESCRIPTION = "CrystalDowsingDesc",
        ICON = "mods/core/talent/explore/crystal_dowsing_icon.png",
        UNLOCK_LEVELS = [5, 10, 15, 20, 25, 50, 75, 100],
        LEVEL_COSTS = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
        COOLDOWNS = [seconds(30), seconds(20), seconds(20), seconds(10), seconds(10), seconds(7), seconds(7), seconds(5)],
        DISTANCES = [300, 300, 500, 500, 700, 700, 900, 1000]
    )

    LIGHT_ORB = AttrDict(
        NAME = "LightOrb",
        DESCRIPTION = "LightOrbDesc",
        ICON = "mods/core/talent/explore/light_orb_icon.png",
        UNLOCK_LEVELS = [6],
        LEVEL_COSTS = [1500],
        COOLDOWN = seconds(1)
    )

    st.BASE_FORM = BASE_FORM
    st.HEAL = HEAL
    st.INTELLIGENCE_BOOST = INTELLIGENCE_BOOST
    st.MIND_BOOST = MIND_BOOST
    st.PILLAR_FORM = PILLAR_FORM
    st.PROTECT = PROTECT
    st.SHELL = SHELL
    st.ENSHROUD_FORM = ENSHROUD_FORM
    st.HASTE = HASTE
    st.DISPEL = DISPEL
    st.VEIL = VEIL
    st.STONESKIN = STONESKIN
    st.RAISE = RAISE
    st.REGENERATE = REGENERATE
    st.INVISIBLE = INVISIBLE
    st.BREATH_FORM
    st.BEAM_FORM = BEAM_FORM
    st.BLAST_FORM = BLAST_FORM
    st.AGILITY_BOOST = AGILITY_BOOST
    st.ATTACK_BOOST = ATTACK_BOOST
    st.DEFENSE_BOOST = DEFENSE_BOOST
    st.FOCUS = FOCUS
    st.BATTLE_CRY = BATTLE_CRY
    st.BERSERK = BERSERK
    st.STUN = STUN
    st.KNOCKBACK = KNOCKBACK
    st.ENSNARE = ENSNARE
    st.SKY_SWORD = SKY_SWORD
    st.SLAM = SLAM
    st.DASH = DASH
    st.TRIPLE_STRIKE = TRIPLE_STRIKE
    st.SPIRIT_ARROW = SPIRIT_ARROW
    st.WALLER = WALLER
    # st.EXPERTISE = EXPERTISE
    st.REFINE = REFINE
    st.POLISH = POLISH
    st.INNOVATE = INNOVATE
    st.COMBAT_CHAOS = COMBAT_CHAOS
    st.SHARPEN = SHARPEN
    st.CATALYST_RESEARCH = CATALYST_RESEARCH
    st.MODIFY_CATALYST = MODIFY_CATALYST
    st.MATERIAL_MASTER = MATERIAL_MASTER
    st.TOOL_PROFICIENCY = TOOL_PROFICIENCY
    st.HEALTH_BOOST = HEALTH_BOOST
    st.TOOL_SPEED = TOOL_SPEED
    st.TOOL_POWER = TOOL_POWER
    st.TOOL_REACH = TOOL_REACH
    st.PICKUP_REACH = PICKUP_REACH
    st.RESOURCEFUL = RESOURCEFUL
    st.BARTER = BARTER
    st.SCAVENGE = SCAVENGE
    st.ORE_HUNTER = ORE_HUNTER
    st.INCREASE_DROP_RATE
    st.PRECISION = PRECISION
    st.STAMINA_BOOST = STAMINA_BOOST
    st.TREASURE_HUNTER = TREASURE_HUNTER
    st.LUCK_BOOST = LUCK_BOOST
    st.SPRINT = SPRINT
    st.JUMP_HEIGHT = JUMP_HEIGHT
    st.DODGE_EXPERTISE = DODGE_EXPERTISE
    st.CARTOGRAPHY = CARTOGRAPHY
    st.LOCKPICK = LOCKPICK
    st.FLARE = FLARE
    st.CRYSTAL_DOWSING = CRYSTAL_DOWSING

    Log.info("Augmented skills")
