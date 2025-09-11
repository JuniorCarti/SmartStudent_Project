# CodeQuest - Python Text Adventure Game

A text-based RPG adventure game built with Python.

## Features

- Player character with inventory and health system
- Multiple interconnected rooms to explore
- Item collection and usage system
- Puzzle solving challenges
- Simple combat mechanics
- Save/load game functionality

## How to Play

1. Run `python main.py` to start the game
2. Use text commands to interact with the world:
   - `go [direction]` - Move in a direction (north, south, east, west)
   - `take [item]` - Pick up an item
   - `use [item]` - Use an item from inventory
   - `inventory` - View your inventory
   - `look` - Examine your surroundings
   - `attack [target]` - Attack a creature
   - `solve [solution]` - Attempt to solve a puzzle
   - `save` - Save your game
   - `load` - Load a saved game
   - `quit` - Exit the game

## Project Structure

The game follows a modular architecture with separate components for:
- Game engine and command parsing
- Entity management (player, creatures)
- World building and room management
- Item system with various item types
- Combat mechanics
- Puzzle system

## Development

This project demonstrates:
- Object-oriented programming principles
- SOLID design patterns
- Modular code architecture
- Unit testing with unittest
- File I/O for save games