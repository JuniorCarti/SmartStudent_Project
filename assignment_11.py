def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Remove first k elements (if k > len(Lin), remove all elements)
    del Lin[:k]
    # Sort the remaining list in ascending order
    Lin.sort()

# Test the function with various cases
def test_remove_and_sort():
    """Test the function with different scenarios"""
    
    print("Testing remove_and_sort function:")
    print("=" * 40)
    
    # Test case 1: Normal removal (from example)
    L1 = [1, 6, 3]
    k1 = 1
    print(f"Test 1: L = {L1}, k = {k1}")
    remove_and_sort(L1, k1)
    print(f"Result: {L1} (Expected: [3, 6])")
    print()
    
    # Test case 2: Remove multiple elements
    L2 = [5, 2, 8, 1, 9, 4]
    k2 = 3
    print(f"Test 2: L = {L2}, k = {k2}")
    remove_and_sort(L2, k2)
    print(f"Result: {L2} (Expected: [1, 4, 9])")
    print()
    
    # Test case 3: Remove all elements
    L3 = [10, 20, 30]
    k3 = 3
    print(f"Test 3: L = {L3}, k = {k3}")
    remove_and_sort(L3, k3)
    print(f"Result: {L3} (Expected: [])")
    print()
    
    # Test case 4: Remove more elements than exist
    L4 = [7, 3, 5]
    k4 = 5
    print(f"Test 4: L = {L4}, k = {k4}")
    remove_and_sort(L4, k4)
    print(f"Result: {L4} (Expected: [])")
    print()
    
    # Test case 5: Remove zero elements
    L5 = [9, 1, 4, 2]
    k5 = 0
    print(f"Test 5: L = {L5}, k = {k5}")
    remove_and_sort(L5, k5)
    print(f"Result: {L5} (Expected: [1, 2, 4, 9])")
    print()
    
    # Test case 6: Empty list
    L6 = []
    k6 = 2
    print(f"Test 6: L = {L6}, k = {k6}")
    remove_and_sort(L6, k6)
    print(f"Result: {L6} (Expected: [])")
    print()
    
    # Test case 7: Negative numbers
    L7 = [-3, 5, -1, 2, -4]
    k7 = 2
    print(f"Test 7: L = {L7}, k = {k7}")
    remove_and_sort(L7, k7)
    print(f"Result: {L7} (Expected: [-4, -1, 2])")
    print()

# Alternative implementation with step-by-step explanation
def remove_and_sort_verbose(Lin, k):
    """Alternative implementation with detailed comments"""
    print(f"Original list: {Lin}")
    print(f"Removing first {k} elements...")
    
    # Check if k is larger than list length
    if k >= len(Lin):
        print("k is larger than list length - removing all elements")
        Lin.clear()
    else:
        # Remove first k elements using slice deletion
        del Lin[:k]
        print(f"After removal: {Lin}")
    
    # Sort the remaining elements
    print("Sorting remaining elements...")
    Lin.sort()
    print(f"Final result: {Lin}")
    print()

# Run the tests
if __name__ == "__main__":
    # Run the basic tests
    test_remove_and_sort()
    
    print("=" * 50)
    print("Detailed step-by-step examples:")
    print("=" * 50)
    
    # Show detailed examples
    L_ex1 = [1, 6, 3]
    remove_and_sort_verbose(L_ex1, 1)
    
    L_ex2 = [5, 2, 8, 1, 9]
    remove_and_sort_verbose(L_ex2, 3)
    
    L_ex3 = [10, 20, 30]
    remove_and_sort_verbose(L_ex3, 5)