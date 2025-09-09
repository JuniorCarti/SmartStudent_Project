def subtract():
    """
    A function that subtracts two numbers entered by the user.
    Handles potential input errors gracefully.
    """
    try:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        print("Result:", a - b)
    except ValueError:
        print("Error: Please enter valid integers!")

# Enhanced version with input validation
def subtract_robust():
    """
    More robust version that ensures valid integer input.
    """
    while True:
        try:
            a = int(input("Enter A: "))
            break
        except ValueError:
            print("Please enter a valid integer for A.")
    
    while True:
        try:
            b = int(input("Enter B: "))
            break
        except ValueError:
            print("Please enter a valid integer for B.")
    
    print("Result:", a - b)

# Version that shows the calculation
def subtract_with_equation():
    """
    Shows the full equation for better user experience.
    """
    try:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        result = a - b
        print(f"{a} - {b} = {result}")
    except ValueError:
        print("Error: Please enter valid integers!")

# Test the functions
if __name__ == "__main__":
    print("Basic version:")
    subtract()
    print()
    
    print("Robust version:")
    subtract_robust()
    print()
    
    print("Equation version:")
    subtract_with_equation()