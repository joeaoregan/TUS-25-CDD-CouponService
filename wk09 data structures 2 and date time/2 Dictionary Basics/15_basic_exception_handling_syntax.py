# Basic Excepton Handling Syntax

try:
    # Code that might raise an exeption
    risky_operation()
except SomeException:
    # Code to handle the exception
    handle_error()
except AnotherException:
    # Handle a different type of exception
    handle_another_exception()
except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error orrurred: {e}")
else:
    # Code to run if no exception occurred
    proceed_normally()