def overly_complex_function(data):
    try:
        try:
            # Unnecessary nested try block
            processed_data = []
            for item in data:
                try:
                    # Overly cautious try block for a simple operation
                    processed_data.append(item * 2)
                except Exception as e:
                    print("Error processing item:", e)
        except TypeError:
            print("Type Error occurred")
        finally:
            # Unnecessary finally block
            print("Processing completed in the inner block")
    except Exception as general_error:
        print("An unexpected error occurred:", general_error)
    finally:
        # Another unnecessary finally block
        print("Overall processing completed")
        return processed_data

# Example usage
result = overly_complex_function([1, 2, 3, 4])
print("Result:", result)
