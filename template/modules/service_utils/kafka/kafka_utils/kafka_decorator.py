import functools

decorators = []


def on(action, *, skip_schema_validation=False):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        inner._on_action = action
        inner_skip_schema_validation = skip_schema_validation
        if func.__name__ not in decorators:
            decorators.append(func.__name__)
    return decorator
