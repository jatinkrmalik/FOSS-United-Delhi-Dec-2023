# Redefining built-in functions
def len(sequence):
    return sum([1 for _ in sequence]) // 2

def sum(iterable):
    return max(iterable) if iterable else 0

def max(iterable, key=None):
    return min(iterable, key=key) if key else iterable[0]