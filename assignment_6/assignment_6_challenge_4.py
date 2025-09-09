def filter_divisible_by_3(numbers):
    """
    Use filter() and lambda to return all numbers divisible by 3 in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        list: Numbers divisible by 3
    """
    # Using filter() with lambda function
    return list(filter(lambda x: x % 3 == 0, numbers))

# Alternative approach using list comprehension
def filter_divisible_by_3_comprehension(numbers):
    """Alternative implementation using list comprehension"""
    return [x for x in numbers if x % 3 == 0]

# Test the function
def test_divisible_by_3():
    """Test function with various test cases"""
    
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],      # Basic case
        [3, 6, 9, 12, 15],                # All divisible by 3
        [1, 2, 4, 5, 7, 8],               # None divisible by 3
        [],                                # Empty list
        [0, 3, 6, 9],                     # Includes zero
        [-3, -6, -9, 2, 4],               # Negative numbers
        [10, 20, 30, 40, 50],             # Some divisible by 3
        [33, 66, 99, 111],                # Larger numbers
        [3.0, 6.0, 7.5]                   # Floats (be careful with floats!)
    ]
    
    print("Numbers Divisible by 3:")
    print("=" * 50)
    
    for i, numbers in enumerate(test_cases, 1):
        result = filter_divisible_by_3(numbers)
        print(f"Test {i}: {numbers}")
        print(f"   Divisible by 3: {result}")
        print("-" * 50)

# Using the function
if __name__ == "__main__":
    # Example with your numbers
    my_numbers = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
    result = filter_divisible_by_3(my_numbers)
    
    print(f"My numbers: {my_numbers}")
    print(f"Numbers divisible by 3: {result}")
    print(f"Count: {len(result)} numbers")
    print()
    
    # Another example
    mixed_numbers = [2, 5, 8, 12, 15, 17, 21, 23, 30]
    result2 = filter_divisible_by_3(mixed_numbers)
    print(f"Mixed numbers: {mixed_numbers}")
    print(f"Divisible by 3: {result2}")
    print()
    
    # Run comprehensive tests
    test_divisible_by_3()
    
    # Show alternative approach
    print("\nUsing list comprehension alternative:")
    test_nums = [1, 3, 5, 6, 9, 10]
    result_comp = filter_divisible_by_3_comprehension(test_nums)
    print(f"Numbers: {test_nums}")
    print(f"Divisible by 3 (comprehension): {result_comp}")