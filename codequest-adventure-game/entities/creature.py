"""
Creature class for enemies and NPCs
"""

class Creature:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.alive = True
        
    def take_damage(self, amount):
        """Take damage"""
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            self.health = 0
            
    def attack(self, target):
        """Attack target"""
        target.take_damage(self.damage)
        return self.damage
        
    def is_alive(self):
        """Check if creature is alive"""
        return self.alive