#Q1. safe_average function

def safe_average(L):
    """
    L is a list of numbers (ints or floats). It may be empty or contain non-numeric values.
    
    Returns the average of all valid numeric elements in the list.
    
    - Ignores non-numeric items using exception handling.
    - If there are no numeric elements, raises a ValueError.
    """
    numeric_values = []
    
    for item in L:
        try:
            # Try to convert to float (handles both int and float)
            numeric_value = float(item)
            numeric_values.append(numeric_value)
        except (ValueError, TypeError):
            # Ignore non-numeric items
            continue
    
    if not numeric_values:
        raise ValueError("No numeric elements found in the list")
    
    return sum(numeric_values) / len(numeric_values)

# Test cases
try:
    print(safe_average([10, 20, "thirty", 40]))  # prints 23.333...
except ValueError as e:
    print(e)

try:
    print(safe_average(["a", "b"]))              # raises ValueError
except ValueError as e:
    print(e)

#Q2. validate_transaction function

def validate_transaction(amounts):
    """
    amounts is a non-empty list of positive integers or floats representing transaction values.
    
    Uses assertions to ensure:
    - the list is not empty
    - all amounts are positive
    Returns the total amount.
    
    Raises AssertionError with a message if validations fail.
    """
    assert len(amounts) > 0, "Transaction list is empty"
    
    for amount in amounts:
        assert amount > 0, "Transaction amount must be positive"
    
    return sum(amounts)

# Test cases
try:
    print(validate_transaction([100, 250.5, 89]))   # prints 439.5
except AssertionError as e:
    print(e)

try:
    print(validate_transaction([]))                # raises AssertionError
except AssertionError as e:
    print(e)

try:
    print(validate_transaction([100, -50]))        # raises AssertionError
except AssertionError as e:
    print(e)


#Q3. student_score_summary function
def student_score_summary(scores, threshold):
    """
    scores: a dictionary mapping student names (str) to total scores (int).
    threshold: an integer score threshold.
    
    Returns a list of student names who scored above the threshold.
    The list should be sorted alphabetically.
    """
    above_threshold = []
    
    for student, score in scores.items():
        if score > threshold:
            above_threshold.append(student)
    
    # Sort the list alphabetically
    above_threshold.sort()
    
    return above_threshold

# Test cases
students = {"Alice": 85, "Bob": 92, "Charlie": 78, "Daisy": 95}
print(student_score_summary(students, 80))   # prints ['Alice', 'Bob', 'Daisy']
print(student_score_summary(students, 100))  # prints []


#Q4. merge_inventory function
def merge_inventory(inv1, inv2):
    """
    inv1 and inv2 are dictionaries mapping item names (str) to quantities (int).
    
    Returns a new dictionary that combines both inventories.
    If an item appears in both, their quantities are summed.
    """
    merged_inv = inv1.copy()  # Start with a copy of the first inventory
    
    for item, quantity in inv2.items():
        if item in merged_inv:
            # Item exists in both inventories, sum the quantities
            merged_inv[item] += quantity
        else:
            # Item only in second inventory, add it
            merged_inv[item] = quantity
    
    return merged_inv

# Alternative solution using dictionary comprehension
def merge_inventory_alt(inv1, inv2):
    merged_inv = {}
    
    # Add all items from first inventory
    for item in set(inv1.keys()) | set(inv2.keys()):
        merged_inv[item] = inv1.get(item, 0) + inv2.get(item, 0)
    
    return merged_inv

# Test case
inv1 = {"pen": 10, "notebook": 5}
inv2 = {"notebook": 3, "eraser": 7}
print(merge_inventory(inv1, inv2))  # prints {'pen': 10, 'notebook': 8, 'eraser': 7}


