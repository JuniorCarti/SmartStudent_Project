# Lambda function to check if a number is a multiple of 3
is_multiple_of_3 = lambda x: x % 3 == 0

# Test the lambda function
test_numbers = [3, 7, 9, 12, 15, 20, 21]

print("Multiples of 3 Check:")
print("=" * 25)
for num in test_numbers:
    result = is_multiple_of_3(num)
    print(f"{num}: {'Yes' if result else 'No'}")