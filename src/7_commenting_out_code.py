def mysterious_function(data):
    # Old implementation (kept for historical reasons)
    # def calculate_sum(numbers):
    #     total = 0
    #     for num in numbers:
    #         total += num
    #     return total
    # result = calculate_sum(data)

    # New approach (experimental)
    def recursive_sum(numbers, index=0):
        if index == len(numbers):
            return 0
        return numbers[index] + recursive_sum(numbers, index + 1)
    return recursive_sum(data)

    # Planned future enhancements
    # TODO: Implement a more efficient summing algorithm
    # TODO: Add error handling for non-numeric input
    # TODO: Optimize for large data sets