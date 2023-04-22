def log_while_exception():
    # This decorator will print the function name when it throws an exception.
    def function_wrapper(func):
        def caller(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exception:
                print(f"'{func.__name__}' throw an exception.")
                raise exception
        return caller
    return function_wrapper