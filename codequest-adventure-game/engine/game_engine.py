"""
Game Engine - Core game loop and state management
"""

import time
from entities.player import Player
from world.world_builder import WorldBuilder
from engine.command_parser import CommandParser
from engine.save_manager import SaveManager
from utils.display import display_room, display_inventory, display_health

class GameEngine:
    def __init__(self):
        self.player = None
        self.world = None
        self.parser = CommandParser()
        self.save_manager = SaveManager()
        self.running = False
        self.current_room = None
        self.messages = []  # For graphical message log
        
    def initialize_game(self):
        """Initialize or load game state"""
        print("Starting new game...")
        time.sleep(1)
        
        # Create player
        self.player = Player("Hero", 100)
        
        # Build world
        self.world = WorldBuilder.build_world()
        self.current_room = self.world.get_room("start_room")
        
        # Add welcome message
        self.add_message("Welcome to CodeQuest Adventure!")
        self.add_message("You stand at the entrance of an ancient dungeon.")
        
        print("Game initialized!")
        
    def run(self):
        """Main game loop for text version"""
        self.initialize_game()
        self.running = True
        
        # Display starting room
        display_room(self.current_room)
        
        while self.running:
            try:
                # Get player input
                command = input("\nWhat would you like to do? ").strip().lower()
                
                if not command:
                    continue
                    
                # Handle quit command
                if command in ["quit", "exit", "q"]:
                    self.running = False
                    continue
                    
                # Parse and execute command
                result = self.execute_command(command)
                
                # Check win/lose conditions
                if self.player.health <= 0:
                    print("You have been defeated! Game Over.")
                    self.running = False
                    
            except KeyboardInterrupt:
                print("\n\nGame interrupted.")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")
                
    def execute_command(self, command):
        """Execute a command and return result"""
        result = self.parser.parse(command, self.player, self.current_room, self.world)
        
        # Handle special commands
        if command.startswith("save"):
            self.save_manager.save_game(self.player, self.world, self.current_room)
            self.add_message("Game saved successfully.")
        elif command.startswith("load"):
            loaded_data = self.save_manager.load_game()
            if loaded_data:
                self.player, self.world, self.current_room = loaded_data
                self.add_message("Game loaded successfully.")
                display_room(self.current_room)
        
        # Update game state if room changed
        if result and hasattr(result, 'room_id'):  # Check if it's a room object
            self.current_room = result
            display_room(self.current_room)
            
        return result
        
    def add_message(self, message):
        """Add a message to the message log"""
        self.messages.append(message)
        if len(self.messages) > 10:  # Keep last 10 messages
            self.messages.pop(0)
        print(f"> {message}")
        
    def get_current_room_data(self):
        """Get data about current room for graphical display"""
        if not self.current_room:
            return None
            
        return {
            'name': self.current_room.name,
            'description': self.current_room.description,
            'items': [{'name': item.name, 'description': item.description} for item in self.current_room.items],
            'creatures': [{'name': creature.name, 'health': creature.health} for creature in self.current_room.creatures],
            'exits': list(self.current_room.exits.keys()),
            'has_puzzle': self.current_room.puzzle is not None
        }
        
    def get_player_data(self):
        """Get player data for graphical display"""
        if not self.player:
            return None
            
        return {
            'name': self.player.name,
            'health': self.player.health,
            'max_health': self.player.max_health,
            'score': getattr(self.player, 'score', 0),
            'inventory': [{'name': item.name, 'description': item.description} for item in self.player.inventory],
            'equipped_weapon': getattr(self.player, 'equipped_weapon', None)
        }
        
    def get_game_state(self):
        """Get complete game state for graphical display"""
        return {
            'room': self.get_current_room_data(),
            'player': self.get_player_data(),
            'messages': self.messages[-5:] if self.messages else []  # Last 5 messages
        }
        
    def handle_graphical_command(self, command_type, data=None):
        """Handle commands from graphical interface"""
        try:
            if command_type == "move":
                direction = data.get('direction')
                if direction:
                    result = self.parser.parse(f"go {direction}", self.player, self.current_room, self.world)
                    if result and hasattr(result, 'room_id'):
                        self.current_room = result
                        self.add_message(f"You go {direction}.")
                        return True
                    else:
                        self.add_message(f"You can't go {direction}.")
                        return False
                        
            elif command_type == "look":
                self.parser.parse("look", self.player, self.current_room, self.world)
                self.add_message("You look around carefully.")
                return True
                
            elif command_type == "use_item":
                item_name = data.get('item_name')
                if item_name:
                    success = self.player.use_item(item_name)
                    if success:
                        self.add_message(f"You used {item_name}.")
                    else:
                        self.add_message(f"Cannot use {item_name} here.")
                    return success
                    
            elif command_type == "attack":
                target_name = data.get('target_name')
                if target_name:
                    result = self.parser.parse(f"attack {target_name}", self.player, self.current_room, self.world)
                    if result is not False:  # Some attacks might return None but still succeed
                        self.add_message(f"You attack {target_name}!")
                        return True
                    return False
                    
            elif command_type == "take_item":
                item_name = data.get('item_name')
                if item_name:
                    result = self.parser.parse(f"take {item_name}", self.player, self.current_room, self.world)
                    if result is not False:
                        self.add_message(f"You take {item_name}.")
                        return True
                    return False
                    
            elif command_type == "solve_puzzle":
                solution = data.get('solution')
                if solution and self.current_room.puzzle:
                    success = self.current_room.puzzle.solve(solution)
                    if success:
                        self.add_message(self.current_room.puzzle.success_message)
                    else:
                        self.add_message("That doesn't seem to work.")
                    return success
                    
            return False
            
        except Exception as e:
            self.add_message(f"Error: {str(e)}")
            return False