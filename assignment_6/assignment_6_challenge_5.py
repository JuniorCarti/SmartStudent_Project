def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Returns a tuple (length, dot product of tA and tB)
    """
    # Check if tuples have the same length
    if len(tA) != len(tB):
        raise ValueError("Tuples must have the same length")
    
    # Calculate dot product
    total = 0
    for i in range(len(tA)):
        total += tA[i] * tB[i]
    
    return (len(tA), total)

# Alternative implementation using zip() and sum()
def dot_product_zip(tA, tB):
    """Alternative implementation using zip() and sum()"""
    if len(tA) != len(tB):
        raise ValueError("Tuples must have the same length")
    
    dot_prod = sum(a * b for a, b in zip(tA, tB))
    return (len(tA), dot_prod)

# Test the function
def test_dot_product():
    """Test function with various test cases"""
    
    test_cases = [
        ((1, 2, 3), (4, 5, 6)),          # Basic case
        ((0, 0), (0, 0)),                # Zeros
        ((1, 1), (1, 1)),                # Ones
        ((-1, 2), (3, -4)),              # Negative numbers
        ((2.5, 3.5), (1.5, 2.5)),        # Floats
        ((10,), (20,)),                  # Single element
        ((1, 2, 3, 4), (5, 6, 7, 8))     # 4-dimensional
    ]
    
    print("Dot Product Calculations:")
    print("=" * 50)
    
    for i, (tA, tB) in enumerate(test_cases, 1):
        try:
            result = dot_product(tA, tB)
            print(f"Test {i}: tA = {tA}, tB = {tB}")
            print(f"   Length: {result[0]}, Dot Product: {result[1]}")
            print("-" * 50)
        except ValueError as e:
            print(f"Test {i}: Error - {e}")
            print("-" * 50)

# Test error case
def test_error_case():
    """Test the error case with different length tuples"""
    print("Testing error case:")
    try:
        result = dot_product((1, 2, 3), (4, 5))
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")
    print("=" * 50)

# Using the function
if __name__ == "__main__":
    # Test the provided examples
    tA = (1, 2, 3)
    tB = (4, 5, 6)
    result = dot_product(tA, tB)
    print(f"tA = {tA}, tB = {tB}")
    print(f"Result: {result}")
    print(f"Length: {result[0]}, Dot Product: {result[1]}")
    print()
    
    # Another example
    tC = (2, 4, 6)
    tD = (1, 3, 5)
    result2 = dot_product(tC, tD)
    print(f"tC = {tC}, tD = {tD}")
    print(f"Result: {result2}")
    print(f"Length: {result2[0]}, Dot Product: {result2[1]}")
    print()
    
    # Run comprehensive tests
    test_dot_product()
    
    # Test error case
    test_error_case()
    
    # Show alternative implementation
    print("Using zip() alternative:")
    result_zip = dot_product_zip(tA, tB)
    print(f"tA = {tA}, tB = {tB}")
    print(f"Result (zip version): {result_zip}")