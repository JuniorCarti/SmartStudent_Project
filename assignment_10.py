# Understanding variable assignment and references
L1 = ['sun']
L2 = L1        # L2 now references the same list object as L1
L1 = ['moon']  # L1 now references a NEW list object, L2 still references the original
print(L2)      # Output: ['sun']

def process_names(names):
    """
    Process a list of names by removing duplicates and sorting alphabetically.
    
    Args:
        names (list): List of names (may contain duplicates)
        
    Returns:
        list: Sorted list with duplicates removed
    """
    # Remove duplicates by converting to set, then back to list
    unique_names = list(set(names))
    
    # Sort alphabetically (case-insensitive sort)
    unique_names.sort(key=lambda x: x.lower())
    
    return unique_names

# Alternative approach preserving original order of first occurrence
def process_names_ordered(names):
    """
    Remove duplicates while preserving order, then sort alphabetically.
    """
    # Remove duplicates while preserving order
    seen = set()
    unique_names = []
    for name in names:
        if name not in seen:
            seen.add(name)
            unique_names.append(name)
    
    # Sort alphabetically
    unique_names.sort(key=lambda x: x.lower())
    return unique_names

# Test the functions
def test_name_processing():
    """Test the name processing functions"""
    
    # Create a list with duplicates
    names = ['Alice', 'bob', 'Charlie', 'alice', 'David', 'Bob', 'eve', 'Charlie', 'Eve']
    
    print("Original list:")
    print(names)
    print(f"Count: {len(names)} names")
    print()
    
    # Process with basic method
    processed1 = process_names(names)
    print("Method 1 - Remove duplicates with set(), then sort:")
    print(processed1)
    print(f"Count: {len(processed1)} unique names")
    print()
    
    # Process with order-preserving method
    processed2 = process_names_ordered(names)
    print("Method 2 - Remove duplicates preserving order, then sort:")
    print(processed2)
    print(f"Count: {len(processed2)} unique names")
    print()
    
    # Show what would happen with regular sort (case-sensitive)
    regular_sort = list(set(names))
    regular_sort.sort()  # Default sort is case-sensitive
    print("Regular sort (case-sensitive):")
    print(regular_sort)
    print("Notice: 'Alice' and 'alice' are treated as different due to case!")
    print()

# Practice: Create list of 10 names with duplicates
def practice_exercise():
    """Practice exercise with 10 names"""
    
    # List of 10 names with intentional duplicates
    names = [
        'John', 'mary', 'John',      # Duplicate: John
        'Alice', 'bob', 'Alice',     # Duplicate: Alice  
        'Charlie', 'david', 'Eve', 'Frank'
    ]
    
    print("Practice Exercise:")
    print("=" * 40)
    print(f"Original names: {names}")
    print(f"Original count: {len(names)}")
    print()
    
    # Remove duplicates and sort
    unique_sorted = process_names(names)
    print(f"After removing duplicates and sorting: {unique_sorted}")
    print(f"Unique count: {len(unique_sorted)}")
    print()
    
    # Show the duplicates that were removed
    from collections import Counter
    count = Counter(names)
    duplicates = {name: count for name, count in count.items() if count > 1}
    
    if duplicates:
        print("Duplicates removed:")
        for name, count in duplicates.items():
            print(f"  {name}: {count} occurrences")
    else:
        print("No duplicates found.")

# Run the programs
if __name__ == "__main__":
    # First, understand the reference behavior
    print("Understanding Variable References:")
    print("=" * 40)
    L1 = ['sun']
    L2 = L1
    print(f"L1 = {L1}, L2 = {L2}")
    L1 = ['moon']
    print(f"After L1 = ['moon']: L1 = {L1}, L2 = {L2}")
    print("L2 still points to the original list!\n")
    
    # Test name processing
    test_name_processing()
    
    # Run practice exercise
    practice_exercise()