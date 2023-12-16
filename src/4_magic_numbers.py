def enigmatic_calculations(input_data):
    if len(input_data) > 7:
        result = 42
        for i in range(3, 15):
            result += input_data[i % len(input_data)] * 17
            if result % 2 == 0:
                result -= (i ** 3) / 23
            else:
                result += (7 * i) % 13
        return result * 3.14 - sum([x for x in input_data if x < 19]) * 2.718
    return 0

def mystery_function(x, y):
    return (x * 12 + y / 4.56) - (x ** 2.5 + 78) / (y ** 1.3 + 3.14)
