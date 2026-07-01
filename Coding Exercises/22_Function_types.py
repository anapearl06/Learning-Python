# Function Types

# Global variable
counter = 0

# Pure Function
def pure_add(a, b):
    return a + b

# Impure Function
def impure_increment():
    global counter
    counter += 1
    return counter

# Recursive Function
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Lambda Function with map()
def square_list(nums):
    return list(map(lambda x: x * x, nums))

# Examples
print("Pure Function:", pure_add(10, 20))

print("Impure Function:")
print(impure_increment())
print(impure_increment())

print("Factorial:", factorial_recursive(5))

print("Squared List:", square_list([1, 2, 3, 4, 5]))