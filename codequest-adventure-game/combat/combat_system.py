"""
Combat System - Handles combat mechanics
"""

import random

class CombatSystem:
    @staticmethod
    def initiate_combat(player, creature):
        """Initiate combat between player and creature"""
        print(f"\n⚔️ Combat with {creature.name}! ⚔️")
        
        while player.is_alive() and creature.is_alive():
            # Player's turn
            damage = CombatSystem.calculate_damage(player, creature)
            creature.take_damage(damage)
            print(f"You attack {creature.name} for {damage} damage!")
            
            if not creature.is_alive():
                print(f"You defeated {creature.name}!")
                return True
                
            # Creature's turn
            damage = CombatSystem.calculate_damage(creature, player)
            player.take_damage(damage)
            print(f"{creature.name} attacks you for {damage} damage!")
            
            if not player.is_alive():
                print("You have been defeated!")
                return False
                
            print(f"Your health: {player.health}, {creature.name}'s health: {creature.health}")
            
        return player.is_alive()
        
    @staticmethod
    def calculate_damage(attacker, defender):
        """Calculate damage with some randomness"""
        base_damage = getattr(attacker, 'damage', 10)
        if hasattr(attacker, 'equipped_weapon') and attacker.equipped_weapon:
            base_damage = attacker.equipped_weapon.damage
            
        # Add some randomness (80-120% of base damage)
        damage = int(base_damage * random.uniform(0.8, 1.2))
        return max(1, damage)  # Ensure at least 1 damage