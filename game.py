"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker, defender):
	weapon = attacker.spell if isinstance(attacker, Magician) and attacker.will_use_spell() else attacker.weapon
	damage, crit = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f'{attacker.name} used {weapon.name}')
	if crit:
		print('Critical hit !')
	print(f'\t{defender.name} took {damage} dmg')

def run_battle(c1, c2):
	pass
