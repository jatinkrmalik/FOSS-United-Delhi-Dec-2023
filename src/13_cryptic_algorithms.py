def cryptic_algo(a, b):
    obscure_factor = 0xABC ^ (a << 2) | (b >> 3)
    mystical_transform = (a * b - (a / b) + a % b) ** 2
    enigmatic_shift = ((mystical_transform << 3) & 0xFF) | obscure_factor
    cryptic_result = (enigmatic_shift ^ 0xDEAD) - ((a & b) * (obscure_factor % 3))
    return cryptic_result

print(cryptic_algo(1,2))