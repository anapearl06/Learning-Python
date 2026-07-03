from functools import wraps

def require_authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_authenticated = True  # Simulating user authentication check
        if not user_authenticated:
            raise PermissionError("User is not authenticated to perform this action.")
        return func(*args, **kwargs)
    return wrapper

@require_authentication
def sensitive_operation():
    print("Performing a sensitive operation that requires authentication.")
    return "Operation completed successfully."


