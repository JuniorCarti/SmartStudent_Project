"""
Battle - Combat sequence management
"""

from combat.combat_system import CombatSystem

class Battle:
    def __init__(self, player, creature):
        self.player = player
        self.creature = creature
        
    def start(self):
        """Start a battle"""
        return CombatSystem.initiate_combat(self.player, self.creature)