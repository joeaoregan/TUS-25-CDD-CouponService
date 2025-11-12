def risky_operation():
    pass

def handle_error():
    pass

def handle_another_exception():
    pass

try:
    # Code that might raise an exception
    risky_operation()
except SomeException:
    # Code to handle the exception
    handle_error()
except AnotherException:
    # Handle a different type of exception
    handle_another_exception()
except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # Code to run if no exception occurred
    proceed_normally()