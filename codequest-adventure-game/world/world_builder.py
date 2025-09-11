"""
World Builder - Constructs the game world
"""

from world.room import Room
from entities.creature import Creature
from items.consumable import HealthPotion
from items.weapon import Sword
from items.key import Key
from world.puzzle import RiddlePuzzle

class WorldBuilder:
    @staticmethod
    def build_world():
        """Build the game world"""
        rooms = {}
        
        # Create rooms
        rooms["start_room"] = Room(
            "start_room", 
            "The Entrance", 
            "You stand at the entrance of an ancient dungeon. Torches flicker on the walls, casting long shadows."
        )
        
        rooms["hallway"] = Room(
            "hallway",
            "Long Hallway",
            "A long, dark hallway stretches before you. The air is damp and cold."
        )
        
        rooms["treasure_room"] = Room(
            "treasure_room",
            "Treasure Room",
            "A glittering room filled with gold and jewels! But something doesn't feel right..."
        )
        
        rooms["puzzle_room"] = Room(
            "puzzle_room",
            "Chamber of Riddles",
            "The walls are covered in ancient runes. A mysterious voice echoes in the room."
        )
        
        # Add exits
        rooms["start_room"].add_exit("north", "hallway")
        rooms["hallway"].add_exit("south", "start_room")
        rooms["hallway"].add_exit("east", "puzzle_room")
        rooms["puzzle_room"].add_exit("west", "hallway")
        rooms["puzzle_room"].add_exit("north", "treasure_room")
        rooms["treasure_room"].add_exit("south", "puzzle_room")
        
        # Add items
        rooms["start_room"].add_item(HealthPotion())
        rooms["hallway"].add_item(Sword())
        
        # Add creatures
        rooms["treasure_room"].add_creature(Creature("Dragon", 50, 15))
        
        # Add puzzle
        riddle = RiddlePuzzle(
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "echo",
            "The door unlocks with a satisfying click!"
        )
        rooms["puzzle_room"].puzzle = riddle
        
        return World(rooms)
    
class World:
    def __init__(self, rooms):
        self.rooms = rooms
        
    def get_room(self, room_id):
        """Get room by ID"""
        return self.rooms.get(room_id)
        
    def add_room(self, room):
        """Add room to world"""
        self.rooms[room.room_id] = room