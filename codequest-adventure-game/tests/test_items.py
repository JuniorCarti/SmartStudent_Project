"""
Unit tests for Items
"""

import unittest
from entities.player import Player
from items.consumable import HealthPotion
from items.weapon import Sword

class TestItems(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer", 100)
        
    def test_health_potion_use(self):
        potion = HealthPotion()
        self.player.health = 80
        potion.use(self.player)
        self.assertEqual(self.player.health, 100)
        
    def test_weapon_equip(self):
        sword = Sword()
        sword.use(self.player)
        self.assertEqual(self.player.equipped_weapon, sword)

if __name__ == "__main__":
    unittest.main()