"""
Unit tests for Combat system
"""

import unittest
from entities.player import Player
from entities.creature import Creature
from combat.combat_system import CombatSystem

class TestCombat(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer", 100)
        self.creature = Creature("Goblin", 30, 5)
        
    def test_combat_initiation(self):
        # Test that combat can be initiated
        result = CombatSystem.initiate_combat(self.player, self.creature)
        self.assertIsInstance(result, bool)
        
    def test_damage_calculation(self):
        damage = CombatSystem.calculate_damage(self.player, self.creature)
        self.assertGreaterEqual(damage, 1)
        
    def test_creature_defeat(self):
        # Test that creature can be defeated
        self.creature.take_damage(30)
        self.assertFalse(self.creature.is_alive())

if __name__ == "__main__":
    unittest.main()