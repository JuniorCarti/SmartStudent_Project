"""
Puzzle system for the game
"""

class Puzzle:
    def __init__(self, description, solution, success_message):
        self.description = description
        self.solution = solution
        self.success_message = success_message
        self.solved = False
        
    def solve(self, attempt):
        """Attempt to solve the puzzle"""
        if attempt.lower() == self.solution.lower():
            self.solved = True
            return True
        return False
        
class RiddlePuzzle(Puzzle):
    def __init__(self, riddle, answer, success_message):
        super().__init__(riddle, answer, success_message)
        self.riddle = riddle
        
    def describe(self):
        """Describe the riddle"""
        return self.riddle