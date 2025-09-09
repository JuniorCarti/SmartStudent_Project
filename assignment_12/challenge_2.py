#1. Functions with Keyword and Default Arguments
# Function with keyword and default arguments
def create_user(name, age, city="Unknown", country="Unknown", is_active=True):
    """
    Create a user profile with optional parameters
    """
    user_profile = {
        "name": name,
        "age": age,
        "city": city,
        "country": country,
        "is_active": is_active
    }
    return user_profile

# Using different calling styles
user1 = create_user("Alice", 25)  # Using defaults
user2 = create_user("Bob", 30, city="New York")  # Mixing positional and keyword
user3 = create_user("Charlie", 35, country="Canada", is_active=False)  # All keyword
user4 = create_user(name="David", age=28, city="London", country="UK")  # All keyword

print(user1)
print(user2)
print(user3)
print(user4)



#2. List Comprehensions from Loops
# Original loop to square numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

# List comprehension equivalent
squared_numbers_comp = [num ** 2 for num in numbers]

print("Loop result:", squared_numbers)
print("List comprehension:", squared_numbers_comp)

# More examples:
# Filter even numbers
evens_loop = []
for num in range(10):
    if num % 2 == 0:
        evens_loop.append(num)

evens_comp = [num for num in range(10) if num % 2 == 0]

# Nested loop to matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_loop = []
for row in matrix:
    for num in row:
        flattened_loop.append(num)

flattened_comp = [num for row in matrix for num in row]

print("Even numbers:", evens_comp)
print("Flattened matrix:", flattened_comp)


#3. Debugging 3 Simple Buggy Programs

#Buggy Program 1: String Concatenation
# Original buggy code
def greet(name):
    print("Hello" + name)  # Missing space

# Fixed code
def greet(name):
    print("Hello " + name)  # Added space
    # Or better: print(f"Hello {name}")

greet("Alice")


#Buggy Program 2: List Modification
# Original buggy code
def double_list(items):
    for item in items:
        item = item * 2  # This doesn't modify the original list
    return items

# Fixed code
def double_list(items):
    return [item * 2 for item in items]  # Create new list
    # Or: for i in range(len(items)): items[i] *= 2

numbers = [1, 2, 3]
print("Doubled:", double_list(numbers))


#Buggy Program 3: Variable Scope
# Original buggy code
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

# This would cause NameError if total is accessed outside
# print(total)  # This would fail

# Fixed code - proper variable scope usage
def calculate_total(price, tax_rate=0.08):
    total = price + (price * tax_rate)
    return total

result = calculate_total(100)
print("Total:", result)


