#Q1. student_score_summary function

def student_score_summary(scores, threshold):
    """
    scores: a dictionary mapping student names (str) to total scores (int).
    threshold: an integer score threshold.
    
    Returns a list of student names who scored above the threshold.
    The list should be sorted alphabetically.
    """
    # Create a list of students who scored above threshold
    high_scorers = []
    
    for student, score in scores.items():
        if score > threshold:
            high_scorers.append(student)
    
    # Sort the list alphabetically
    high_scorers.sort()
    
    return high_scorers

# Test cases
students = {"Alice": 85, "Bob": 92, "Charlie": 78, "Daisy": 95}
print(student_score_summary(students, 80))   # prints ['Alice', 'Bob', 'Daisy']
print(student_score_summary(students, 100))  # prints []


#Q2. merge_inventory function

def merge_inventory(inv1, inv2):
    """
    inv1 and inv2 are dictionaries mapping item names (str) to quantities (int).
    
    Returns a new dictionary that combines both inventories.
    If an item appears in both, their quantities are summed.
    """
    # Create a copy of the first inventory
    merged = inv1.copy()
    
    # Add items from second inventory
    for item, quantity in inv2.items():
        if item in merged:
            # Item exists in both, sum the quantities
            merged[item] += quantity
        else:
            # New item, add to merged inventory
            merged[item] = quantity
    
    return merged

# Alternative solution using dictionary comprehension
def merge_inventory_alt(inv1, inv2):
    """
    Alternative implementation using set operations
    """
    merged = {}
    
    # Get all unique items from both inventories
    all_items = set(inv1.keys()) | set(inv2.keys())
    
    for item in all_items:
        # Sum quantities from both inventories (0 if item doesn't exist)
        merged[item] = inv1.get(item, 0) + inv2.get(item, 0)
    
    return merged

# Test cases
inv1 = {"pen": 10, "notebook": 5}
inv2 = {"notebook": 3, "eraser": 7}
print(merge_inventory(inv1, inv2))  # prints {'pen': 10, 'notebook': 8, 'eraser': 7}


#Additional Test Cases

print(merge_inventory_alt(inv1, inv2))  # prints {'pen': 10, 'notebook': 8, 'eraser': 7}