#!/usr/bin/env python3
"""
Quick fix for testing the game
"""

import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine.game_engine import GameEngine
from utils.display import display_welcome

def test_game():
    """Test the game with fixed commands"""
    display_welcome()
    
    # Initialize game engine
    game = GameEngine()
    game.initialize_game()
    
    # Test basic commands
    print("\n=== Testing basic commands ===")
    
    # Test look command
    print("\nTesting 'look' command:")
    game.parser.parse("look", game.player, game.current_room, game.world)
    
    # Test take command
    print("\nTesting 'take' command:")
    game.parser.parse("take health potion", game.player, game.current_room, game.world)
    
    # Test inventory command
    print("\nTesting 'inventory' command:")
    game.parser.parse("inventory", game.player, game.current_room, game.world)
    
    # Test go command
    print("\nTesting 'go' command:")
    result = game.parser.parse("go north", game.player, game.current_room, game.world)
    if result:
        game.current_room = result
        game.parser.parse("look", game.player, game.current_room, game.world)
    
    # Test help command
    print("\nTesting 'help' command:")
    game.parser.parse("help", game.player, game.current_room, game.world)
    
    print("\n=== Basic test completed ===")

if __name__ == "__main__":
    test_game()