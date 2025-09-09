def total_letters(string_list):
    """
    Calculate the total number of letters in a list of strings.
    
    Args:
        string_list (list): List of strings
        
    Returns:
        int: Total number of letters across all strings
    """
    # Using sum() with generator expression
    return sum(len(word) for word in string_list)

# Alternative approach using map()
def total_letters_map(string_list):
    """Alternative implementation using map()"""
    return sum(map(len, string_list))

# Test the function
def test_total_letters():
    """Test function with various test cases"""
    
    test_cases = [
        ["hello", "world"],           # Basic case
        ["python", "is", "awesome"],  # Multiple words
        [""],                         # Empty string
        [],                           # Empty list
        ["a", "bb", "ccc", "dddd"],   # Different lengths
        ["123", "45", "6"],           # Numbers (still count as characters)
        ["hello world"],              # String with space
        ["@#$%", "&*!"],              # Special characters
        ["αβγ", "δεζ"]               # Unicode characters
    ]
    
    print("Total Letters Calculation:")
    print("=" * 50)
    
    for i, strings in enumerate(test_cases, 1):
        total = total_letters(strings)
        print(f"Test {i}: {strings}")
        print(f"   Individual lengths: {[len(s) for s in strings]}")
        print(f"   Total letters: {total}")
        print("-" * 50)

# Using the function
if __name__ == "__main__":
    # Example usage
    words = ["function", "signature", "python"]
    result = total_letters(words)
    print(f"Words: {words}")
    print(f"Total letters: {result}")
    print()
    
    # Another example
    sentence = ["This", "is", "a", "sentence"]
    result2 = total_letters(sentence)
    print(f"Sentence words: {sentence}")
    print(f"Total letters: {result2}")
    print()
    
    # Run comprehensive tests
    test_total_letters()
    
    # Demonstrate alternative approach
    print("\nUsing map() alternative:")
    test_words = ["hello", "world"]
    result_map = total_letters_map(test_words)
    print(f"Words: {test_words}")
    print(f"Total letters (map version): {result_map}")