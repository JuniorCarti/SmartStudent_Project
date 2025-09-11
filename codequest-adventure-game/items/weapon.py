"""
Weapon items
"""

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def use(self, player):
        """Equip the weapon"""
        player.equipped_weapon = self
        print(f"You equip the {self.name}.")
        return False  # Don't consume the item
        
class Sword(Weapon):
    def __init__(self):
        super().__init__("Iron Sword", 15)