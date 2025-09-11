"""
Unit tests for Player class
"""

import unittest
from entities.player import Player
from items.consumable import HealthPotion

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer", 100)
        
    def test_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.max_health, 100)
        self.assertEqual(self.player.inventory, [])
        
    def test_add_item(self):
        potion = HealthPotion()
        self.player.add_item(potion)
        self.assertIn(potion, self.player.inventory)
        
    def test_remove_item(self):
        potion = HealthPotion()
        self.player.add_item(potion)
        self.player.remove_item(potion)
        self.assertNotIn(potion, self.player.inventory)
        
    def test_take_damage(self):
        self.player.take_damage(20)
        self.assertEqual(self.player.health, 80)
        
    def test_heal(self):
        self.player.health = 80
        self.player.heal(20)
        self.assertEqual(self.player.health, 100)
        
    def test_heal_over_max(self):
        self.player.health = 95
        self.player.heal(20)
        self.assertEqual(self.player.health, 100)

if __name__ == "__main__":
    unittest.main()