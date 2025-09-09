def digit_frequency_counter():
    """
    Counts how often each digit (0-9) appears in a given number string.
    Uses dictionary comprehension and demonstrates multiple approaches.
    """
    
    # Get input from user
    number_string = input("Enter a number or sequence of digits: ").strip()
    
    # Validate input - ensure it contains only digits
    if not number_string.isdigit():
        print("Error: Please enter only digits (0-9)!")
        return
    
    # Initialize a dictionary with all digits 0-9 set to count 0
    digit_counts = {str(digit): 0 for digit in range(10)}
    
    # Count occurrences of each digit using a for loop
    for char in number_string:
        if char in digit_counts:
            digit_counts[char] += 1
    
    # Display results in a formatted table
    print("\n" + "="*30)
    print("DIGIT FREQUENCY REPORT")
    print("="*30)
    print(f"{'Digit':<10} {'Frequency':<10} {'Bar Chart':<10}")
    print("-" * 30)
    
    for digit, count in sorted(digit_counts.items()):
        # Create a simple bar chart visualization
        bar = '█' * count if count > 0 else '─'
        print(f"{digit:<10} {count:<10} {bar}")
    
    print("="*30)
    
    # Additional analysis
    most_frequent = max(digit_counts.items(), key=lambda x: x[1])
    least_frequent = min(digit_counts.items(), key=lambda x: x[1])
    
    print(f"\nMost frequent digit: {most_frequent[0]} (appears {most_frequent[1]} times)")
    print(f"Least frequent digit: {least_frequent[0]} (appears {least_frequent[1]} times)")
    print(f"Total digits analyzed: {len(number_string)}")

# Alternative approach using collections.Counter (more Pythonic)
def digit_frequency_counter_advanced():
    from collections import Counter
    
    number_string = input("Enter a number or sequence of digits: ").strip()
    
    if not number_string.isdigit():
        print("Error: Please enter only digits (0-9)!")
        return
    
    # Count all characters (will include non-digits if present)
    counter = Counter(number_string)
    
    # Filter for only digits and ensure all 0-9 are represented
    digit_counts = {str(d): counter.get(str(d), 0) for d in range(10)}
    
    # Display results
    print("\nAdvanced Analysis:")
    for digit, count in sorted(digit_counts.items()):
        percentage = (count / len(number_string)) * 100 if len(number_string) > 0 else 0
        print(f"Digit {digit}: {count} times ({percentage:.1f}%)")

# Run the main function
if __name__ == "__main__":
    digit_frequency_counter()
    print("\n" + "="*50)
    
