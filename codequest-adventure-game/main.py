#!/usr/bin/env python3
"""
CodeQuest - Python Text Adventure Game
Main entry point for the game with PyGame graphical interface
"""

import sys
import os
import pygame

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pygame_ui.game_window import GameWindow
from utils.display import display_welcome, display_game_over

def main():
    """Main game function with graphical interface selection"""
    print("CodeQuest Adventure Game")
    print("========================")
    print("1. Text-based version (console)")
    print("2. Graphical version (PyGame)")
    
    choice = input("Choose version (1 or 2): ").strip()
    
    if choice == "2":
        # Run graphical version
        run_graphical_version()
    else:
        # Run text version
        run_text_version()

def run_text_version():
    """Run the original text-based version"""
    display_welcome()
    
    # Initialize game engine
    from engine.game_engine import GameEngine
    game = GameEngine()
    
    try:
        # Main game loop
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        display_game_over()

def run_graphical_version():
    """Run the PyGame graphical version"""
    try:
        # Initialize pygame
        pygame.init()
        
        # Create and run game window
        game = GameWindow()
        game.run()
        
    except Exception as e:
        print(f"Error in graphical version: {e}")
        print("Falling back to text version...")
        run_text_version()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()