"""
Unit tests for World
"""

import unittest
from world.room import Room
from world.world_builder import WorldBuilder

class TestWorld(unittest.TestCase):
    def test_room_creation(self):
        room = Room("test_room", "Test Room", "A test room")
        self.assertEqual(room.name, "Test Room")
        
    def test_world_building(self):
        world = WorldBuilder.build_world()
        self.assertIsNotNone(world.get_room("start_room"))

if __name__ == "__main__":
    unittest.main()