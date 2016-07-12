from coremod import overload
from siege.component import Stat, Stats


@overload
def createCombatStats(**kwargs):
    stats = Stats()
    stats.stats.append(Stat('HP', 'HP', kwargs.get('HP', 100), 99999, True, True))
    stats.stats.append(Stat('SP', 'SP', kwargs.get('SP', 100), 99999, True, True))
    stats.stats.append(Stat('ATK', 'Attack', kwargs.get('ATK', 100), 9999, False, True))
    stats.stats.append(Stat('DEF', 'Defense', kwargs.get('DEF', 100), 9999, False, True))
    stats.stats.append(Stat('INT', 'Intelligence', kwargs.get('INT', 100), 9999, False, True))
    stats.stats.append(Stat('MIND', 'Mind', kwargs.get('MIND', 100), 9999, False, True))
    stats.stats.append(Stat('AGI', 'Agility', kwargs.get('AGI', 100), 9999, False, True))
    stats.stats.append(Stat('LUCK', 'Luck', kwargs.get('LUCK', 100), 9999, False, True))
    stats.stats.append(Stat('ACC', 'Accuracy', kwargs.get('ACC', 0), 9999, False, False))
    stats.stats.append(Stat('EVA', 'Evasion', kwargs.get('EVA', 0), 9999, False, False))
    stats.stats.append(Stat('SPD', 'Attack Speed', kwargs.get('SPD', 0), 50, False, False))
    stats.stats.append(Stat('MOVE', 'Movement Speed', kwargs.get('MOVE', 100), 9999, False, False))
    stats.stats.append(Stat('HPRegen', 'HP Regeneration', kwargs.get('HPRegen', 0), 9999, False, False))
    stats.stats.append(Stat('SPRegen', 'SP Regeneration', kwargs.get('SPRegen', 30), 9999, False, False))
    stats.stats.append(Stat('knockback', 'Knockback Power', kwargs.get('knockback', 0), 9999, False, False))
    stats.stats.append(Stat('knockbackRes', 'Knockback Resistance', kwargs.get('knockbackRes', 0), 9999, False, False))
    stats.stats.append(Stat('physicalReduction', 'Physical Reduction', kwargs.get('physicalReduction', 0), 100, False, False))
    stats.stats.append(Stat('magicalReduction', 'Magical Reduction', kwargs.get('magicalReduction', 0), 100, False, False))
    return stats
