#Lecture 15 Challenge 1: recur_factorial

def recur_factorial(n):
    """
    n: int >= 0

    Returns the factorial of n using recursion.
    Hint: Base case is when n == 0. In the recursive case, return n * factorial(n-1).
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * recur_factorial(n - 1)

# Examples:
print(recur_factorial(0))  # prints 1
print(recur_factorial(5))  # prints 120
print(recur_factorial(7))  # prints 5040


#Lecture 15 Challenge 2: is_palindrome_recur

def is_palindrome_recur(s):
    """
    s: string

    Returns True if s is a palindrome using recursion, False otherwise.
    Hint: A string is a palindrome if the first and last characters are equal
    and the substring in between is also a palindrome.
    """
    # Base case 1: empty string or single character is always a palindrome
    if len(s) <= 1:
        return True
    
    # Base case 2: if first and last characters don't match, it's not a palindrome
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check if the substring (excluding first and last characters) is a palindrome
    return is_palindrome_recur(s[1:-1])

# Alternative implementation with more explicit base cases
def is_palindrome_recur_alt(s):
    """
    Alternative implementation with more detailed base cases
    """
    # Remove any spaces and convert to lowercase for case-insensitive check
    s_clean = s.replace(" ", "").lower()
    
    # Base cases
    if len(s_clean) <= 1:
        return True
    if s_clean[0] != s_clean[-1]:
        return False
    
    # Recursive step
    return is_palindrome_recur_alt(s_clean[1:-1])

# Examples:
print(is_palindrome_recur("racecar"))  # prints True
print(is_palindrome_recur("hello"))    # prints False
print(is_palindrome_recur("madam"))    # prints True

# Additional test cases
print(is_palindrome_recur("a"))        # prints True (single character)
print(is_palindrome_recur(""))         # prints True (empty string)
print(is_palindrome_recur("level"))    # prints True
print(is_palindrome_recur("python"))   # prints False


#Iterative Versions for Comparison:

# Iterative factorial for comparison
def iterative_factorial(n):
    """
    Iterative version of factorial
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Iterative palindrome check for comparison
def iterative_palindrome(s):
    """
    Iterative version of palindrome check
    """
    s_clean = s.replace(" ", "").lower()
    left = 0
    right = len(s_clean) - 1
    
    while left < right:
        if s_clean[left] != s_clean[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Compare recursive vs iterative
print("\nComparison:")
print("Recursive factorial(5):", recur_factorial(5))
print("Iterative factorial(5):", iterative_factorial(5))
print("Recursive palindrome('racecar'):", is_palindrome_recur("racecar"))
print("Iterative palindrome('racecar'):", iterative_palindrome("racecar"))