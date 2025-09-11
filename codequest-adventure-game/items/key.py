"""
Key items for progression
"""

class Key:
    def __init__(self, name, door_id):
        self.name = name
        self.door_id = door_id
        
    def use(self, player):
        """Key usage - typically context specific"""
        print(f"The {self.name} might unlock something...")
        return False  # Keys aren't consumed on use