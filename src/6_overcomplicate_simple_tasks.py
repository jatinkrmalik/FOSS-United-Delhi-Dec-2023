def unnecessarily_complex_check(input_value):
    def _recursive_checker(n, depth=0):
        if depth > 4:
            return n % 2 == 0
        else:
            return _recursive_checker(n + 1, depth + 1) if n % 3 != 0 else _recursive_checker(n - 1, depth + 1)

    adjusted_value = sum([ord(c) for c in str(input_value)]) if isinstance(input_value, str) else input_value
    intermediate_result = adjusted_value * 3 - 7
    return _recursive_checker(intermediate_result)

result = unnecessarily_complex_check(42)
print(result)