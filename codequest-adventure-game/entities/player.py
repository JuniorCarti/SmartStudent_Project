"""
Player class representing the game player
"""

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.max_health = health
        self.inventory = []
        self.equipped_weapon = None
        self.location = None
        self.score = 0   # ✅ Track player's score (for PyGame + text versions)

    def add_item(self, item):
        """Add item to inventory"""
        self.inventory.append(item)
        print(f"Added {item.name} to inventory.")

    def remove_item(self, item):
        """Remove item from inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def use_item(self, item_name):
        """Use item from inventory"""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                result = item.use(self)
                if result:
                    self.inventory.remove(item)
                return result
        print(f"You don't have {item_name}.")
        return False

    def take_damage(self, amount):
        """Reduce player health"""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        """Heal player"""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def is_alive(self):
        """Check if player is alive"""
        return self.health > 0

    def add_score(self, points):
        """Increase player score"""
        self.score += points
        print(f"🏆 {self.name} gained {points} points! (Total: {self.score})")

    def display_status(self):
        """Display player status"""
        print(f"\n=== {self.name} ===")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Score: {self.score}")  # ✅ Display score
        print("Inventory:", [item.name for item in self.inventory])
        if self.equipped_weapon:
            print(f"Equipped: {self.equipped_weapon.name}")
