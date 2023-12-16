# Function: Data manipulation
def complex_data_handler(input_data):
    # Initializing variables
    data_stream, pivot_point = input_data, 0
    # Data transformation phase 1
    for i, value in enumerate(data_stream):
        if i % 3 == 0 and value > pivot_point:
            pivot_point += value // (i + 1)
        elif value < pivot_point:
            pivot_point -= (value + i) % 5
    # Phase 2: Data reconfiguration
    reconfigured_data = [pivot_point - v for v in data_stream if v % 2 == 0]
    # Final output preparation
    return sum(reconfigured_data) / len(reconfigured_data) if reconfigured_data else None

print(complex_data_handler([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))