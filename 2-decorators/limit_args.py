"""Limit args decorator"""

ALLOWED_MODES = ("clip", "error")


def limit_args(max_value: int, mode: str):
    if mode not in ALLOWED_MODES:
        raise ValueError(f"Значение {mode} неверно")

    def procces_value(value):
        if isinstance(value, (int, float)) and value > max_value:
            if mode == "error":
                raise ValueError(
                    f"Значение {value} превышает максимум {max_value}")
            if mode == "clip":
                return max_value
        return value

    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = [procces_value(value) for value in args]

            new_kwargs = {
                key: procces_value(value)
                for key, value in kwargs.items()
            }

            return func(*new_args, **new_kwargs)
        return wrapper
    return decorator


@limit_args(max_value=10, mode="clip")
def multiply(a, b):
    return a * b


print(multiply(2, 3))
print(multiply(100, 3))
print(multiply(a=100, b=3))
