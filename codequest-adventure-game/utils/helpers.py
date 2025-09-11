"""
Helper utilities for the game
"""

import random

def random_chance(percent):
    """Return True with given percent chance"""
    return random.random() < (percent / 100)

def format_list(items):
    """Format a list of items for display"""
    if not items:
        return "nothing"
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]