#Lecture 16 Challenge 3: count_occurrences_nested

def count_occurrences_nested(L, target):
    """
    L: a list that may contain other lists (nested)
    target: any value

    Returns the number of times target appears anywhere in L, including nested sublists.
    """
    count = 0
    
    for item in L:
        if isinstance(item, list):
            # If item is a list, recursively count occurrences in the nested list
            count += count_occurrences_nested(item, target)
        else:
            # If item is not a list, check if it matches the target
            if item == target:
                count += 1
    
    return count

# Examples:
print(count_occurrences_nested([1, [2, [1, 3], 4], 1], 1))  # prints 3
print(count_occurrences_nested([[1,2],[3,[4,1]]], 4))       # prints 1
print(count_occurrences_nested([[],[],[]], 5))              # prints 0

# Additional test cases
print(count_occurrences_nested([1, 2, 3, 1, 1], 1))        # prints 3 (no nesting)
print(count_occurrences_nested([[[1]], [1, [1]]], 1))      # prints 3 (deep nesting)


#Lecture 16 Challenge 4: hanoi_moves

def hanoi_moves(n, source, target, spare):
    """
    n: int >= 1
    source, target, spare: string names of rods (e.g. "A", "B", "C")

    Returns a list of strings representing the sequence of moves needed
    to solve the Towers of Hanoi puzzle.
    """
    if n == 1:
        # Base case: move single disk from source to target
        return [f"Move from {source} to {target}"]
    else:
        # Recursive case:
        # 1. Move n-1 disks from source to spare (using target as spare)
        moves1 = hanoi_moves(n-1, source, spare, target)
        
        # 2. Move the largest disk from source to target
        moves2 = [f"Move from {source} to {target}"]
        
        # 3. Move n-1 disks from spare to target (using source as spare)
        moves3 = hanoi_moves(n-1, spare, target, source)
        
        # Combine all moves
        return moves1 + moves2 + moves3

# Examples:
print(hanoi_moves(2, 'A', 'C', 'B'))
# prints ['Move from A to B', 'Move from A to C', 'Move from B to C']

print(hanoi_moves(3, 'A', 'C', 'B'))
# For 3 disks: 7 moves total
# prints ['Move from A to C', 'Move from A to B', 'Move from C to B', 
#         'Move from A to C', 'Move from B to A', 'Move from B to C', 
#         'Move from A to C']

# Additional test case
print("\nHanoi with 1 disk:")
print(hanoi_moves(1, 'A', 'C', 'B'))  # prints ['Move from A to C']


#Memoization Example
# Memoization for Fibonacci sequence (to show the concept)
def fibonacci(n, memo={}):
    """
    Demonstrates memoization with Fibonacci sequence
    """
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Compare with non-memoized version
def fibonacci_slow(n):
    if n <= 2:
        return 1
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

print("\nFibonacci with memoization:")
print(fibonacci(10))  # Fast due to memoization
print(fibonacci(20))  # Still fast

print("\nFibonacci without memoization (will be slow for larger numbers):")
print(fibonacci_slow(10))  # OK for small numbers
# print(fibonacci_slow(35))  # This would be very slow!