def labyrinthine_logic(data):
    if data and len(data) > 5:
        if all(isinstance(x, int) for x in data):
            result = 0
            for i in range(len(data)):
                if i % 2 == 0:
                    for j in range(1, i + 1):
                        if data[j] % j == 0:
                            result += j * (data[j] - i)
                            for k in range(j, 0, -1):
                                if k in data:
                                    result -= k
                                    if result < 0:
                                        result *= -1
                                        for m in range(5):
                                            result += m ** 2 if m % 2 == 0 else m
    else:
        result = None
    return result