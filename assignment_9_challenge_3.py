def is_even(n):
    """
    Check if a number is even with proper input validation.
    
    Args:
        n: Input to check
        
    Returns:
        bool: True if n is even, False if odd
        
    Raises:
        ValueError: If input is not an integer
    """
    if not isinstance(n, int):
        raise ValueError("Invalid input: input must be an integer")
    return n % 2 == 0

# Enhanced version with better error messages and type conversion
def is_even_robust(n):
    """
    More robust version that attempts to convert to integer.
    
    Args:
        n: Input to check (can be string or integer)
        
    Returns:
        bool: True if n is even, False if odd
        
    Raises:
        ValueError: If input cannot be converted to integer
    """
    # Try to convert to integer if it's a string
    if isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            raise ValueError(f"Invalid input: '{n}' cannot be converted to integer")
    elif not isinstance(n, int):
        raise ValueError(f"Invalid input: expected integer, got {type(n).__name__}")
    
    return n % 2 == 0

# Version that returns result with status message
def check_even_with_message(n):
    """
    Returns a tuple with success status and message.
    """
    try:
        result = is_even_robust(n)
        return (True, "Even" if result else "Odd")
    except ValueError as e:
        return (False, str(e))

# Test the functions
def test_even_functions():
    """Test the even-checking functions with various inputs"""
    
    print("Testing is_even function:")
    print("=" * 50)
    
    # Test valid inputs
    valid_test_cases = [2, 4, 0, -6, 7, -3, 100, 999]
    for n in valid_test_cases:
        try:
            result = is_even(n)
            status = "Even" if result else "Odd"
            print(f"✓ {n}: {status}")
        except ValueError as e:
            print(f"✗ {n}: {e}")
    print()
    
    # Test invalid inputs
    invalid_test_cases = [3.14, "hello", [1, 2], None, "12.5", True]
    print("Testing invalid inputs (should raise ValueError):")
    for n in invalid_test_cases:
        try:
            result = is_even(n)
            print(f"✗ {n} (type: {type(n).__name__}): Unexpectedly passed")
        except ValueError as e:
            print(f"✓ {n} (type: {type(n).__name__}): {e}")
    print()
    
    # Test robust version
    print("Testing robust version (is_even_robust):")
    robust_test_cases = [10, "20", "abc", 15.5, "7", "-4", "3.14", 0]
    for n in robust_test_cases:
        try:
            result = is_even_robust(n)
            status = "Even" if result else "Odd"
            print(f"✓ {n} (type: {type(n).__name__}): {status}")
        except ValueError as e:
            print(f"✗ {n} (type: {type(n).__name__}): {e}")
    print()
    
    # Test message version
    print("Testing check_even_with_message:")
    message_test_cases = [8, "6", "not_a_number", 5, 2.5]
    for n in message_test_cases:
        success, message = check_even_with_message(n)
        symbol = "✓" if success else "✗"
        print(f"{symbol} {n}: {message}")

# Example usage
if __name__ == "__main__":
    # Basic examples
    print("Basic raise examples:")
    print("-" * 25)
    
    # Valid cases
    try:
        print(f"4 is even: {is_even(4)}")
        print(f"7 is even: {is_even(7)}")
        print(f"0 is even: {is_even(0)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Invalid case - will raise ValueError
    try:
        print(f"3.14 is even: {is_even(3.14)}")
    except ValueError as e:
        print(f"Correctly caught: {e}")
    
    print("\n" + "="*50)
    
    # Run comprehensive tests
    test_even_functions()