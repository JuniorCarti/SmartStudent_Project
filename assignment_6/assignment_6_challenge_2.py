def calculate_average(numbers):
    """
    Calculate the average of a list of numbers using sum() and len().
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: The average of the numbers
    """
    # Check for empty list to avoid division by zero
    if len(numbers) == 0:
        return 0.0
    
    # Calculate average: sum of numbers divided by count of numbers
    return sum(numbers) / len(numbers)

# Test the function
def test_average_calculation():
    """Test function with various test cases"""
    
    test_cases = [
        [1, 2, 3, 4, 5],          # Basic case
        [10, 20, 30],             # Another basic case
        [5],                      # Single element
        [],                       # Empty list
        [2.5, 3.5, 4.5],         # Float numbers
        [-1, 0, 1],              # Negative and zero
        [100, 200, 300, 400]     # Larger numbers
    ]
    
    print("Average Calculations:")
    print("=" * 40)
    
    for i, numbers in enumerate(test_cases, 1):
        average = calculate_average(numbers)
        print(f"Test {i}: {numbers}")
        print(f"   Sum: {sum(numbers)}")
        print(f"   Count: {len(numbers)}")
        print(f"   Average: {average:.2f}")
        print("-" * 40)

# Alternative one-liner version
def calculate_average_concise(numbers):
    """Concise version using ternary operator"""
    return sum(numbers) / len(numbers) if numbers else 0.0

# Using the function
if __name__ == "__main__":
    # Example usage
    grades = [85, 92, 78, 90, 88]
    average_grade = calculate_average(grades)
    print(f"Grades: {grades}")
    print(f"Average grade: {average_grade:.2f}")
    print()
    
    # Run comprehensive tests
    test_average_calculation()