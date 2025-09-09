#Assignment 1: Library Book Tracker

class Book:
    def __init__(self, title, author, year, copies_available):
        """
        Initialize a Book with title, author, year, and copies available
        """
        self.title = title
        self.author = author
        self.year = year
        self.copies_available = copies_available
    
    def borrow(self):
        """
        Decrease copies_available by 1 if at least one copy is available
        Otherwise print "Not available."
        """
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"Book borrowed. {self.copies_available} copies remaining.")
        else:
            print("Not available.")
    
    def return_book(self):
        """
        Increase copies_available by 1
        """
        self.copies_available += 1
        print(f"Book returned. {self.copies_available} copies available.")
    
    def is_same_book(self, other):
        """
        Returns True if title and author match another book object
        """
        return self.title == other.title and self.author == other.author
    
    def __str__(self):
        """
        String representation of the Book
        """
        return f"'{self.title}' by {self.author} ({self.year}), Copies: {self.copies_available}"

# Test the Book class
print("📘 Library Book Tracker Tests:")
b1 = Book("Python Basics", "Dennis Omboga", 2024, 3)
b2 = Book("Python Basics", "Dennis Omboga", 2024, 2)

print("Initial state:")
print(b1)
print(b2)

print("\nBorrowing and returning:")
b1.borrow()          # reduces to 2
b1.borrow()          # reduces to 1
b1.return_book()     # increases to 2

print(f"\nAre b1 and b2 the same book? {b1.is_same_book(b2)}")  # True

# Additional tests
print("\n🧪 Additional Book Tests:")
b3 = Book("Advanced Python", "Jane Smith", 2023, 1)
b4 = Book("Advanced Python", "John Doe", 2023, 1)

print(f"Are b3 and b4 the same book? {b3.is_same_book(b4)}")  # False (different authors)

# Test borrowing when no copies available
b5 = Book("Test Book", "Test Author", 2024, 1)
b5.borrow()  # Should work
b5.borrow()  # Should print "Not available."


#Assignment 2: Fraction Calculator with Dunder Methods

import math

class Fraction:
    def __init__(self, num, denom):
        """
        Initialize a Fraction with numerator and denominator
        """
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = num
        self.denom = denom
        self.simplify()  # Simplify on creation
    
    def simplify(self):
        """
        Reduce the fraction to its simplest form
        """
        gcd = math.gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd
        
        # Handle negative signs
        if self.denom < 0:
            self.num = -self.num
            self.denom = -self.denom
    
    def __add__(self, other):
        """
        Add two fractions using the formula: a/b + c/d = (a*d + b*c)/(b*d)
        Returns a new Fraction object
        """
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)
    
    def __eq__(self, other):
        """
        Return True if fractions are equal (e.g., 1/2 == 2/4)
        """
        # Compare simplified fractions
        return self.num == other.num and self.denom == other.denom
    
    def __str__(self):
        """
        Return "num/denom" format
        """
        if self.denom == 1:
            return str(self.num)
        return f"{self.num}/{self.denom}"
    
    # Bonus: Additional dunder methods
    def __sub__(self, other):
        """Subtract two fractions"""
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)
    
    def __mul__(self, other):
        """Multiply two fractions"""
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

# Test the Fraction class
print("\n📗 Fraction Calculator Tests:")
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = f1 + f2  # 1/2 + 1/4 = 3/4

print(f"f1 = {f1}")      # 1/2
print(f"f2 = {f2}")      # 1/4
print(f"f1 + f2 = {f3}") # 3/4

print(f"f1 == f2: {f1 == f2}")                # False
print(f"f1 == Fraction(2, 4): {f1 == Fraction(2, 4)}")  # True

# Additional tests
print("\n🧪 Additional Fraction Tests:")
f4 = Fraction(2, 3)
f5 = Fraction(3, 4)
print(f"f4 + f5 = {f4 + f5}")  # 17/12
print(f"f4 - f5 = {f4 - f5}")  # -1/12
print(f"f4 * f5 = {f4 * f5}")  # 6/12 = 1/2

# Test simplification
f6 = Fraction(4, 8)
print(f"4/8 simplified: {f6}")  # 1/2

# Test whole numbers
f7 = Fraction(6, 2)
print(f"6/2 simplified: {f7}")  # 3