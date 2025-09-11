"""
Complexity Analysis Assignment
Python Implementation of Various Algorithms with Complexity Analysis
"""

import time
import matplotlib.pyplot as plt
import numpy as np

# 1. Mystery Function Analysis
def mystery(L):
    """
    Function with unknown complexity - to be analyzed.
    """
    total = 0
    for i in range(len(L)):
        for j in range(i):
            total += L[j]
    return total

# 2. Binary Search Implementation
def binary_search(arr, target):
    """
    Binary search algorithm with Θ(log n) complexity.
    Returns index of target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# 3. Fibonacci Implementations
def fib_recur(n):
    """
    Recursive Fibonacci implementation with Θ(2ⁿ) complexity.
    """
    if n <= 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)

def fib_iter(n):
    """
    Iterative Fibonacci implementation with Θ(n) complexity.
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# 4. Runtime Comparison and Analysis
def time_function(func, n, *args):
    """
    Measure execution time of a function.
    """
    start = time.time()
    result = func(n, *args) if args else func(n)
    end = time.time()
    return end - start, result

def compare_fibonacci_runtimes():
    """
    Compare runtime of recursive vs iterative Fibonacci implementations.
    Generates and saves a PNG plot of the results.
    """
    n_values = list(range(10, 41, 5))
    recur_times = []
    iter_times = []
    results = []

    print("Fibonacci Runtime Comparison:")
    print("n\tRecursive Time\tIterative Time\tResult")
    print("-" * 50)
    
    for n in n_values:
        time_recur, result_recur = time_function(fib_recur, n)
        time_iter, result_iter = time_function(fib_iter, n)
        
        # Verify both implementations give the same result
        assert result_recur == result_iter, f"Results differ for n={n}"
        
        recur_times.append(time_recur)
        iter_times.append(time_iter)
        results.append(result_recur)
        
        print(f"{n}\t{time_recur:.6f}s\t\t{time_iter:.6f}s\t\t{result_recur}")

    # Plot the results
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(n_values, recur_times, 'ro-', label='Recursive Fibonacci (Θ(2ⁿ))', linewidth=2)
    plt.plot(n_values, iter_times, 'bo-', label='Iterative Fibonacci (Θ(n))', linewidth=2)
    plt.xlabel('n (Fibonacci number to compute)')
    plt.ylabel('Time (seconds)')
    plt.title('Runtime Comparison: Recursive vs Iterative Fibonacci')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.semilogy(n_values, recur_times, 'ro-', label='Recursive Fibonacci (Θ(2ⁿ))', linewidth=2)
    plt.semilogy(n_values, iter_times, 'bo-', label='Iterative Fibonacci (Θ(n))', linewidth=2)
    plt.xlabel('n (Fibonacci number to compute)')
    plt.ylabel('Time (seconds) - Log Scale')
    plt.title('Runtime Comparison (Logarithmic Scale)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot as a PNG file
    plt.savefig('fibonacci_runtime_comparison.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'fibonacci_runtime_comparison.png'")
    
    plt.show()
    
    return n_values, recur_times, iter_times, results

# 5. Generate theoretical complexity curves for comparison
def generate_complexity_curves():
    """
    Generate theoretical complexity curves for educational purposes.
    """
    n_values = np.linspace(1, 40, 100)
    
    # Theoretical complexities (normalized for comparison)
    constant = np.ones_like(n_values)
    logarithmic = np.log2(n_values)
    linear = n_values
    linearithmic = n_values * np.log2(n_values)
    quadratic = n_values ** 2
    exponential = 2 ** (n_values / 5)  # Scaled for visualization
    
    # Normalize all curves to similar range for comparison
    constant = constant / np.max(constant)
    logarithmic = logarithmic / np.max(logarithmic)
    linear = linear / np.max(linear)
    linearithmic = linearithmic / np.max(linearithmic)
    quadratic = quadratic / np.max(quadratic)
    exponential = exponential / np.max(exponential)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, constant, label='Constant Θ(1)', linewidth=2)
    plt.plot(n_values, logarithmic, label='Logarithmic Θ(log n)', linewidth=2)
    plt.plot(n_values, linear, label='Linear Θ(n)', linewidth=2)
    plt.plot(n_values, linearithmic, label='Linearithmic Θ(n log n)', linewidth=2)
    plt.plot(n_values, quadratic, label='Quadratic Θ(n²)', linewidth=2)
    plt.plot(n_values, exponential, label='Exponential Θ(2ⁿ) (scaled)', linewidth=2)
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Normalized Runtime')
    plt.title('Theoretical Complexity Curves')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('theoretical_complexity_curves.png', dpi=300, bbox_inches='tight')
    print("Theoretical complexity curves saved as 'theoretical_complexity_curves.png'")
    
    plt.show()

# Test the functions
if __name__ == "__main__":
    # Test mystery function
    test_list = [1, 2, 3, 4, 5]
    print(f"mystery({test_list}) = {mystery(test_list)}")
    
    # Test binary search
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11
    result_idx = binary_search(sorted_arr, target)
    print(f"Binary search for {target} in {sorted_arr}: index {result_idx}")
    
    # Compare Fibonacci runtimes (this will generate and save the PNG)
    n_vals, recur_t, iter_t, fib_results = compare_fibonacci_runtimes()
    
    # Generate theoretical complexity curves
    generate_complexity_curves()
    
    print("\nAll plots have been generated and saved as PNG files.")