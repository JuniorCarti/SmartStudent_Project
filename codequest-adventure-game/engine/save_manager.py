"""
Save Manager - Handles saving and loading game progress
"""

import json
import os

class SaveManager:
    def __init__(self, save_dir="saves"):
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)
        
    def save_game(self, player, world, current_room):
        """Save game state to file"""
        save_data = {
            "player": {
                "name": player.name,
                "health": player.health,
                "max_health": player.max_health,
                "inventory": [item.__class__.__name__ for item in player.inventory],
            },
            "current_room": current_room.room_id,
            "world": self._serialize_world(world)
        }
        
        save_path = os.path.join(self.save_dir, "savegame.json")
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=2)
            
        print("Game saved successfully!")
        return True
        
    def load_game(self):
        """Load game state from file"""
        save_path = os.path.join(self.save_dir, "savegame.json")
        
        if not os.path.exists(save_path):
            print("No saved game found!")
            return None
            
        try:
            with open(save_path, 'r') as f:
                save_data = json.load(f)
                
            # Reconstruct player
            from entities.player import Player
            player = Player(
                save_data["player"]["name"],
                save_data["player"]["max_health"]
            )
            player.health = save_data["player"]["health"]
            
            # Reconstruct inventory (simplified)
            from items.consumable import HealthPotion
            from items.weapon import Sword
            for item_class in save_data["player"]["inventory"]:
                if item_class == "HealthPotion":
                    player.add_item(HealthPotion())
                elif item_class == "Sword":
                    player.add_item(Sword())
            
            # Reconstruct world
            from world.world_builder import WorldBuilder
            world = WorldBuilder.build_world()
            
            # Set current room
            current_room = world.get_room(save_data["current_room"])
            
            print("Game loaded successfully!")
            return player, world, current_room
            
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
            
    def _serialize_world(self, world):
        """Serialize world state (simplified)"""
        # In a real implementation, you'd track which rooms have been visited,
        # which items have been collected, which puzzles are solved, etc.
        return {"version": "1.0"}