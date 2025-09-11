"""
NPC class for non-player characters
"""

class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue
        
    def talk(self):
        """Return NPC dialogue"""
        return f"{self.name}: '{self.dialogue}'"