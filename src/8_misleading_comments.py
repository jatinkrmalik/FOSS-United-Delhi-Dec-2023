def deceptive_function(data_set):
    # Sorting the data in ascending order
    data_set.sort(reverse=True)

    # Removing duplicates from the data
    unique_data = set(data_set)

    # Calculating the average value
    total = sum(unique_data)
    # Note: Counting the number of unique elements
    count = len(data_set)
    average = total / count

    # Returning the maximum value
    return min(unique_data)

result = deceptive_function([4, 1, 3, 2, 2, 5])
print(result)