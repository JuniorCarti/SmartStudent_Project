"""
Command Parser - Processes player input
"""

class CommandParser:
    def __init__(self):
        self.commands = {
            "go": self.handle_go,
            "move": self.handle_go,
            "take": self.handle_take,
            "get": self.handle_take,
            "use": self.handle_use,
            "inventory": self.handle_inventory,
            "look": self.handle_look,
            "examine": self.handle_examine,
            "attack": self.handle_attack,
            "health": self.handle_health,
            "solve": self.handle_solve,
            "help": self.handle_help,
            "save": self.handle_save,
            "load": self.handle_load,
        }
        
    def parse(self, command, player, current_room, world):
        """Parse and execute player command"""
        parts = command.split()
        if not parts:
            return None
            
        verb = parts[0]
        obj = " ".join(parts[1:]) if len(parts) > 1 else None
        
        if verb in self.commands:
            return self.commands[verb](player, current_room, world, obj)
        else:
            print("I don't understand that command. Try 'help' for available commands.")
            return None
            
    def handle_go(self, player, current_room, world, direction):
        """Handle movement commands"""
        if not direction:
            print("Go where?")
            return None
            
        if direction in current_room.exits:
            next_room_id = current_room.exits[direction]
            next_room = world.get_room(next_room_id)
            if next_room:
                print(f"You go {direction}.")
                return next_room
            else:
                print("That way is blocked.")
        else:
            print("You can't go that way.")
        return None
        
    def handle_take(self, player, current_room, world, item_name):
        """Handle item collection"""
        if not item_name:
            print("Take what?")
            return None
            
        for item in current_room.items[:]:
            if item.name.lower() == item_name.lower():
                player.add_item(item)
                current_room.remove_item(item)
                return None
                
        print(f"You don't see {item_name} here.")
        return None
        
    def handle_use(self, player, current_room, world, item_name):
        """Handle item usage"""
        if not item_name:
            print("Use what?")
            return None
            
        player.use_item(item_name)
        return None
        
    def handle_inventory(self, player, current_room, world, obj):
        """Show inventory"""
        player.display_status()
        return None
        
    def handle_look(self, player, current_room, world, obj):
        """Look around or at specific object"""
        if not obj:
            print(current_room.describe())
        else:
            print(f"You examine {obj} but don't see anything special.")
        return None
        
    def handle_examine(self, player, current_room, world, obj):
        """Examine object"""
        self.handle_look(player, current_room, world, obj)
        return None
        
    def handle_attack(self, player, current_room, world, target):
        """Handle attack commands"""
        if not target:
            print("Attack what?")
            return None
            
        # Check if target exists in current room
        target_creature = None
        for creature in current_room.creatures:
            if creature.name.lower() == target.lower():
                target_creature = creature
                break
                
        if target_creature:
            from combat.battle import Battle
            battle = Battle(player, target_creature)
            result = battle.start()
            
            if result:  # Player won
                current_room.remove_creature(target_creature)
                print(f"You defeated {target_creature.name}!")
            return None
        else:
            print(f"You don't see {target} here.")
            return None
        
    def handle_health(self, player, current_room, world, obj):
        """Show health status"""
        print(f"Health: {player.health}/{player.max_health}")
        return None
        
    def handle_solve(self, player, current_room, world, solution):
        """Solve puzzles"""
        if current_room.puzzle:
            if not solution:
                print("Solve what? Provide a solution.")
                return None
                
            if current_room.puzzle.solve(solution):
                print(current_room.puzzle.success_message)
                # Puzzle solved actions could go here
            else:
                print("That doesn't seem to work.")
        else:
            print("There's nothing to solve here.")
        return None
        
    def handle_help(self, player, current_room, world, obj):
        """Show help information"""
        print("\nAvailable commands:")
        print("  go [direction] - Move in a direction (north, south, east, west)")
        print("  take [item] - Pick up an item")
        print("  use [item] - Use an item from inventory")
        print("  inventory - View your inventory")
        print("  look - Examine your surroundings")
        print("  attack [target] - Attack a creature")
        print("  solve [solution] - Attempt to solve a puzzle")
        print("  save - Save your game")
        print("  load - Load a saved game")
        print("  health - Show your health status")
        print("  help - Show this help message")
        print("  quit - Exit the game")
        return None
        
    def handle_save(self, player, current_room, world, obj):
        """Handle save command"""
        from engine.save_manager import SaveManager
        save_manager = SaveManager()
        save_manager.save_game(player, world, current_room)
        return None
        
    def handle_load(self, player, current_room, world, obj):
        """Handle load command"""
        from engine.save_manager import SaveManager
        save_manager = SaveManager()
        loaded_data = save_manager.load_game()
        if loaded_data:
            return loaded_data
        return None