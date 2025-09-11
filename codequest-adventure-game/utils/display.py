"""
Display utilities for the game
"""

def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("          CODEQUEST - TEXT ADVENTURE")
    print("=" * 50)
    print("Welcome to CodeQuest! Your adventure begins...")
    print("Type 'help' for commands or 'quit' to exit.")
    print()

def display_game_over():
    """Display game over message"""
    print("\n" + "=" * 50)
    print("          THANKS FOR PLAYING CODEQUEST!")
    print("=" * 50)

def display_room(room):
    """Display room description"""
    print(room.describe())

def display_inventory(items):
    """Display inventory"""
    if not items:
        print("Your inventory is empty.")
    else:
        print("Inventory:")
        for item in items:
            print(f"  - {item.name}")

def display_health(player):
    """Display health status"""
    print(f"Health: {player.health}/{player.max_health}")