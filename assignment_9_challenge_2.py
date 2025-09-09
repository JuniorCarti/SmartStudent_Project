def check_age(age):
    """
    Check if age is non-negative using assert statement.
    
    Args:
        age (int): The age to validate
        
    Raises:
        AssertionError: If age is negative
    """
    assert age >= 0, "Age can't be negative"
    print("Age is okay.")

# Enhanced version with better error handling
def check_age_robust(age):
    """
    More robust version that handles various input types and edge cases.
    """
    # Convert to integer if possible
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise ValueError("Age must be a valid integer")
    
    # Check if age is non-negative
    assert age >= 0, "Age can't be negative"
    print(f"Age {age} is valid.")

# Version that returns boolean instead of using assert
def is_valid_age(age):
    """
    Check if age is valid without using assert.
    Returns True if valid, False otherwise.
    """
    try:
        age_int = int(age)
        return age_int >= 0
    except (ValueError, TypeError):
        return False

# Test the functions
def test_age_functions():
    """Test the age validation functions with various inputs"""
    
    print("Testing check_age function:")
    print("=" * 40)
    
    # Test cases that should work
    test_cases_valid = [0, 1, 25, 100, "0", "25"]
    for age in test_cases_valid:
        try:
            check_age(age)
            print(f"✓ {age} (type: {type(age).__name__}) - Valid")
        except (AssertionError, ValueError) as e:
            print(f"✗ {age} - Error: {e}")
    print()
    
    # Test cases that should fail
    test_cases_invalid = [-1, -5, "-3", "abc", None, 3.14]
    print("Testing invalid ages (should raise errors):")
    for age in test_cases_invalid:
        try:
            check_age(age)
            print(f"✗ {age} (type: {type(age).__name__}) - Unexpectedly passed")
        except AssertionError as e:
            print(f"✓ {age} - Correctly caught: {e}")
        except ValueError as e:
            print(f"✓ {age} - Correctly caught: {e}")
        except Exception as e:
            print(f"✗ {age} - Unexpected error: {e}")
    print()
    
    # Test the robust version
    print("Testing robust version:")
    robust_test_cases = [30, -5, "25", "abc", 0]
    for age in robust_test_cases:
        try:
            check_age_robust(age)
            print(f"✓ {age} - Valid")
        except Exception as e:
            print(f"✗ {age} - Error: {e}")
    print()
    
    # Test the boolean version
    print("Testing boolean version (is_valid_age):")
    bool_test_cases = [10, -2, "15", "hello", 0, -1, 3.5]
    for age in bool_test_cases:
        result = is_valid_age(age)
        status = "Valid" if result else "Invalid"
        print(f"{age}: {status}")

# Run the tests
if __name__ == "__main__":
    # Basic usage examples
    print("Basic assert examples:")
    print("-" * 20)
    
    # This will work
    try:
        check_age(25)
    except AssertionError as e:
        print(f"Error: {e}")
    
    # This will raise AssertionError
    try:
        check_age(-5)
    except AssertionError as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50)
    
    # Run comprehensive tests
    test_age_functions()