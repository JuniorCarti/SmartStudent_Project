def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Remove first k elements (if k > len(Lin), remove all elements
    del Lin[:k]
    # Sort the remaining list in ascending order
    Lin.sort()

# Test cases
def test_remove_and_sort():
    """Test the function with various cases"""
    
    print("Testing remove_and_sort function:")
    print("=" * 40)
    
    # Test case 1: Normal removal
    L1 = [1, 6, 3]
    k1 = 1
    print(f"Original: {L1}, k = {k1}")
    remove_and_sort(L1, k1)
    print(f"After: {L1}")
    print("-" * 20)
    
    # Test case 2: Remove multiple elements
    L2 = [5, 2, 8, 1, 9]
    k2 = 3
    print(f"Original: {L2}, k = {k2}")
    remove_and_sort(L2, k2)
    print(f"After: {L2}")
    print("-" * 20)
    
    # Test case 3: Remove more elements than exist
    L3 = [10, 20, 30]
    k3 = 5
    print(f"Original: {L3}, k = {k3}")
    remove_and_sort(L3, k3)
    print(f"After: {L3}")
    print("-" * 20)
    
    # Test case 4: Remove all elements
    L4 = [7, 3, 5]
    k4 = 3
    print(f"Original: {L4}, k = {k4}")
    remove_and_sort(L4, k4)
    print(f"After: {L4}")
    print("-" * 20)
    
    # Test case 5: Remove zero elements
    L5 = [9, 1, 4, 2]
    k5 = 0
    print(f"Original: {L5}, k = {k5}")
    remove_and_sort(L5, k5)
    print(f"After: {L5}")
    print("-" * 20)
    
    # Test case 6: Empty list
    L6 = []
    k6 = 2
    print(f"Original: {L6}, k = {k6}")
    remove_and_sort(L6, k6)
    print(f"After: {L6}")
    print("-" * 20)

# Alternative implementation with explicit checks
def remove_and_sort_verbose(Lin, k):
    """More explicit version showing the logic step-by-step"""
    # Handle case where k is larger than list length
    if k >= len(Lin):
        # Remove all elements
        Lin.clear()
    else:
        # Remove first k elements
        for _ in range(k):
            if Lin:  # Check if list is not empty
                Lin.pop(0)
        # Sort the remaining elements
        Lin.sort()

# Run the tests
if __name__ == "__main__":
    test_remove_and_sort()
    
    # Additional edge cases
    print("\nAdditional Edge Cases:")
    print("=" * 40)
    
    # Negative numbers
    L7 = [-3, 5, -1, 2, -4]
    k7 = 2
    print(f"Original: {L7}, k = {k7}")
    remove_and_sort(L7, k7)
    print(f"After: {L7}")
    print("-" * 20)
    
    # Duplicate values
    L8 = [3, 1, 3, 2, 1]
    k8 = 2
    print(f"Original: {L8}, k = {k8}")
    remove_and_sort(L8, k8)
    print(f"After: {L8}")
    print("-" * 20)