"""
Room class representing locations in the game world
"""

class Room:
    def __init__(self, room_id, name, description, exits=None, items=None, creatures=None, puzzle=None):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.exits = exits or {}
        self.items = items or []
        self.creatures = creatures or []
        self.puzzle = puzzle
        self.visited = False
        
    def add_exit(self, direction, room_id):
        """Add an exit to the room"""
        self.exits[direction] = room_id
        
    def remove_exit(self, direction):
        """Remove an exit from the room"""
        if direction in self.exits:
            del self.exits[direction]
            
    def add_item(self, item):
        """Add item to room"""
        self.items.append(item)
        
    def remove_item(self, item):
        """Remove item from room"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
        
    def add_creature(self, creature):
        """Add creature to room"""
        self.creatures.append(creature)
        
    def remove_creature(self, creature):
        """Remove creature from room"""
        if creature in self.creatures:
            self.creatures.remove(creature)
            return True
        return False
        
    def get_exit_directions(self):
        """Get available exit directions"""
        return list(self.exits.keys())
        
    def get_exit_room(self, direction):
        """Get room ID for exit direction"""
        return self.exits.get(direction)
        
    def describe(self):
        """Generate room description"""
        description = f"\n=== {self.name} ===\n{self.description}\n"
        
        if self.items:
            description += "\nYou see: " + ", ".join([item.name for item in self.items])
            
        if self.creatures:
            description += "\nCreatures here: " + ", ".join([creature.name for creature in self.creatures])
            
        if self.exits:
            description += f"\nExits: {', '.join(self.get_exit_directions())}"
            
        return description