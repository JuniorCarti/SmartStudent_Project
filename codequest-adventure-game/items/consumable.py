"""
Consumable items
"""

class Consumable:
    def __init__(self, name, effect_value):
        self.name = name
        self.effect_value = effect_value
        
    def use(self, player):
        """Use the consumable item"""
        raise NotImplementedError("Subclasses must implement use()")
        
class HealthPotion(Consumable):
    def __init__(self):
        super().__init__("Health Potion", 20)
        
    def use(self, player):
        """Restore health"""
        player.heal(self.effect_value)
        print(f"You drink the Health Potion and restore {self.effect_value} health!")
        return True