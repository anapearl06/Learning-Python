# Caching Expensive Calculations

def cache_results(func):
    cache = {}

    def wrapper(a, b):
        if (a, b) in cache:
            return f"From Cache: {cache[(a, b)]}"

        result = func(a, b)
        cache[(a, b)] = result
        return f"Computed: {result}"

    return wrapper


@cache_results
def multiply(a, b):
    return a * b


# Example
print(multiply(5, 4))
print(multiply(5, 4))
print(multiply(2, 8))
print(multiply(2, 8))