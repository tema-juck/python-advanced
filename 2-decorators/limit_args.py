"""Limit args decorator"""


def limit_args(max_value: int, mode: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = list(args)

            for index, value in enumerate(new_args):
                if value > max_value and isinstance(value, int):
                    if mode == "error":
                        raise ValueError

                    if mode == "clip":
                        new_args[index] = max_value

            return func(*new_args, **kwargs)
        return wrapper
    return decorator


@limit_args(max_value=10, mode="clip")
def multiply(a, b):
    return a * b


print(multiply(2, 3))
print(multiply(100, 3))
