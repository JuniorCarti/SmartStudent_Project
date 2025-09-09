#Q1. Timing Functions

import time

# Loop-based sum function
def sum_with_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Formula-based sum function
def sum_with_formula(n):
    return n * (n + 1) // 2

# Timing comparison
n_values = [10**3, 10**5, 10**7]

print("Timing Comparison:")
print("n\t\tLoop (s)\tFormula (s)")
print("-" * 40)

for n in n_values:
    # Time loop version
    start_time = time.time()
    result_loop = sum_with_loop(n)
    loop_time = time.time() - start_time
    
    # Time formula version
    start_time = time.time()
    result_formula = sum_with_formula(n)
    formula_time = time.time() - start_time
    
    print(f"{n:<10}\t{loop_time:.6f}\t\t{formula_time:.6f}")

#The loop-based function has O(n) time complexity because it performs n additions. The formula-based function has O(1) constant time complexity since it performs only 3 operations regardless of input size. As n increases, the loop version takes significantly longer while the formula version remains nearly instantaneous.

#Q2. Counting Operations

def sum_with_loop_count(n):
    operations = 0
    total = 0
    operations += 1  # assignment
    
    for i in range(1, n + 1):
        total += i
        operations += 2  # addition and assignment
    
    operations += 1  # return
    return total, operations

# Test with different n values
n_values = [10, 100, 1000]
print("Operation Count Analysis:")
print("n\tOperations\tBig-O")
print("-" * 30)

for n in n_values:
    result, ops = sum_with_loop_count(n)
    print(f"{n}\t{ops}\t\tO(n)")

#Big-O Notation: O(n) - The number of operations grows linearly with input size n.

#Part 2: Complexity Analysis

#Q3. Linear vs Quadratic Growth

def linear_sum(L):
    operations = 0
    total = 0
    operations += 1  # assignment
    
    for x in L:
        total += x
        operations += 2  # addition and assignment
    
    operations += 1  # return
    return total, operations

def quadratic_pairs(L):
    operations = 0
    count = 0
    operations += 1  # assignment
    
    for i in L:
        for j in L:
            count += i * j
            operations += 3  # multiplication, addition, assignment
    
    operations += 1  # return
    return count, operations

# Analysis
import matplotlib.pyplot as plt
import numpy as np

# Test with increasing input sizes
sizes = [10, 20, 50, 100, 200]
linear_ops = []
quadratic_ops = []

for size in sizes:
    L = list(range(size))
    
    _, linear_op_count = linear_sum(L)
    linear_ops.append(linear_op_count)
    
    _, quadratic_op_count = quadratic_pairs(L)
    quadratic_ops.append(quadratic_op_count)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_ops, 'b-o', label='Linear Sum O(n)')
plt.plot(sizes, quadratic_ops, 'r-o', label='Quadratic Pairs O(n²)')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Operations')
plt.title('Linear vs Quadratic Growth')
plt.legend()
plt.grid(True)
plt.show()

print("Complexity Analysis:")
print("Linear Sum: O(n), Θ(n)")
print("Quadratic Pairs: O(n²), Θ(n²)")


#Q4. Searching Algorithms

def linear_search(arr, target):
    operations = 0
    for i, element in enumerate(arr):
        operations += 1  # comparison
        if element == target:
            operations += 1  # return
            return i, operations
    operations += 1  # return (not found)
    return -1, operations

def binary_search(arr, target):
    operations = 0
    low, high = 0, len(arr) - 1
    operations += 2  # assignments
    
    while low <= high:
        operations += 1  # comparison
        mid = (low + high) // 2
        operations += 1  # calculation
        
        if arr[mid] == target:
            operations += 1  # return
            return mid, operations
        elif arr[mid] < target:
            low = mid + 1
            operations += 2  # comparison and assignment
        else:
            high = mid - 1
            operations += 2  # comparison and assignment
    
    operations += 1  # return (not found)
    return -1, operations

# Comparison
import random

sizes = [10**3, 10**4, 10**5, 10**6]
linear_results = []
binary_results = []
builtin_results = []

for size in sizes:
    arr = sorted(random.sample(range(size * 2), size))
    target = random.choice(arr)  # Ensure target exists
    
    # Linear search
    _, linear_ops = linear_search(arr, target)
    linear_results.append(linear_ops)
    
    # Binary search
    _, binary_ops = binary_search(arr, target)
    binary_results.append(binary_ops)
    
    # Built-in in operator (approximate)
    start_time = time.time()
    target in arr
    builtin_time = time.time() - start_time
    builtin_results.append(builtin_time * 1e6)  # Convert to microseconds

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(sizes, linear_results, 'r-o', label='Linear Search Θ(n)')
plt.plot(sizes, binary_results, 'b-o', label='Binary Search Θ(log n)')
plt.xlabel('Input Size')
plt.ylabel('Operations')
plt.title('Search Algorithm Complexity')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(sizes, builtin_results, 'g-o', label='Built-in "in" operator')
plt.xlabel('Input Size')
plt.ylabel('Time (microseconds)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("Complexity Analysis:")
print("Linear Search: Θ(n) - worst case examines every element")
print("Binary Search: Θ(log n) - halves search space each iteration")
print("Built-in 'in' operator: Uses optimized search (often similar to binary search for sorted data)")


#Part 3: Applied Analysis

#Q5. Matrix Multiplication

def matrix_multiply(A, B):
    n = len(A)
    operations = 0
    
    # Initialize result matrix
    C = [[0 for _ in range(n)] for _ in range(n)]
    operations += n * n  # Initialization
    
    # Matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                operations += 2  # multiplication and addition
    
    operations += 1  # return
    return C, operations

# Test with different matrix sizes
matrix_sizes = [2, 5, 10, 20]
operations_count = []

for size in matrix_sizes:
    A = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    B = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    
    result, ops = matrix_multiply(A, B)
    operations_count.append(ops)
    
    print(f"Matrix {size}x{size}: {ops} operations")

# Complexity analysis
print(f"\nComplexity: O(n³), Θ(n³)")
print("Three nested loops each running n times → n * n * n = n³ operations")


#Q6. Best, Worst, and Average Case

def linear_search_cases(arr, target):
    best_case_ops = 0
    worst_case_ops = 0
    average_case_ops = 0
    
    # Best case (element first)
    best_case_ops += 1  # first comparison
    if arr[0] == target:
        best_case_ops += 1  # return
        best_index = 0
    else:
        best_case_ops = float('inf')  # not actually best case
    
    # Worst case (element last or missing)
    for i, element in enumerate(arr):
        worst_case_ops += 1  # comparison
        if element == target and i == len(arr) - 1:
            worst_case_ops += 1  # return
            worst_index = i
            break
        elif i == len(arr) - 1:
            worst_case_ops += 1  # return (not found)
            worst_index = -1
    
    # Average case (middle element)
    mid = len(arr) // 2
    average_case_ops += mid + 1  # comparisons to reach middle
    if arr[mid] == target:
        average_case_ops += 1  # return
        average_index = mid
    else:
        average_case_ops = len(arr)  # approximate average
    
    return best_case_ops, worst_case_ops, average_case_ops

# Test analysis
test_arr = list(range(1000))
target_first = 0
target_middle = 500
target_last = 999
target_missing = 1000

print("Best/Worst/Average Case Analysis:")
print("Target\tBest\tWorst\tAverage")
print("-" * 40)

for target, description in [(target_first, "First"), (target_middle, "Middle"), 
                           (target_last, "Last"), (target_missing, "Missing")]:
    best, worst, avg = linear_search_cases(test_arr, target)
    print(f"{description}\t{best}\t{worst}\t{avg}")

print("\nComplexity Classification:")
print("Best case: O(1), Θ(1) - constant time (element found immediately)")
print("Worst case: O(n), Θ(n) - linear time (element last or missing)")
print("Average case: O(n), Θ(n) - linear time (element in the middle)")