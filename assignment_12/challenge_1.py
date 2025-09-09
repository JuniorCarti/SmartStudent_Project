#1. Fix the Code
def subtract():
    a = int(input("Enter number: "))  # Convert to int
    b = int(input("Enter number: "))  # Convert to int
    print("Result:", a - b)

#2. Add assert to This Code
    def check_age(age):
      assert age >= 0, "Age cannot be negative"  # Added assertion
    print("Age is okay.")

    #3. Use raise to catch invalid input

    def is_even(n):
       if not isinstance(n, int):  # Check if n is not an integer
        raise TypeError("Input must be an integer")  # Raise exception
    return n % 2 == 0