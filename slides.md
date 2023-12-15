%title: The Coder's Guide to Job Security
%author: @jatinkrmalik
%date: 2023-12-16

-> # The Coder's Guide to Job Security <-

^

-> **Mastering the Art of Confusing Code!** <- 

^

-> > Jatin K Malik <-


---

Welcome to a journey through the mystical art of writing *unmaintainable* code. 

Guarantee your job for life - because no one else will dare to touch your code!

Let's get started!

---

# Why Write Unmaintainable Code?

- **Job Security:** The more confusing your code, the more indispensable you become.
- **Challenge:** Test the limits of your ingenuity in obfuscation.
- **Fun:** Let's be honest, it's amusing to watch others struggle with your creative genius.

Ready to dive into the art of confusion?

---

# Rule #1: Naming Conventions

```python
def mysteryOrbitLauncher(nuclearFusionGenerator):
    antimatterReactorOutput = 1
    for quantumFluctuation in range(1, nuclearFusionGenerator + 1):
        antimatterReactorOutput *= quantumFluctuation
    return antimatterReactorOutput
    
interstellarTravelSpeed = 5
warpDriveCapacity = mysteryOrbitLauncher(interstellarTravelSpeed)
logger.Debug("Warp Drive Capacity at Speed", interstellarTravelSpeed, ":", warpDriveCapacity)
```

- Keep them guessing what each variable and function does!

^

- This is just a simple factorial function, but the naming conventions make it look like a complex space travel simulation.

---

# Rule #2: Documentation

```python
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
```

- Provide general and unhelpful comments like "Data transformation phase 1" and "Final output preparation".
- Avoid explaining the purpose behind specific operations or logic.
- Use comments to give a false sense of understanding, while the actual code remains cryptic.

---

# Rule #3: Code Structure


```python
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
```

- Nest conditions like Russian dolls.
- The deeper, the better.

---


# Rule #4: Inconsistent Style


```python
class dataProcessor:
    def __init__(self, DataInput):
        self.dataInput = DataInput

    def ProcessData(self):
        processed_data = []
        for index, value in enumerate(self.dataInput):
            if index % 2 == 0:
                processed_data.append(value * 2)
            else:
                processed_data.append(value + 5)
        return processed_data

    def calculateStatistics(self, data):
        MeanValue = sum(data) / len(data)
        maxValue = max(data)
        return {"mean": MeanValue, "max": maxValue}

def analyzeDATA(data_set):
    processor = dataProcessor(data_set)
    processedData = processor.ProcessData()
    return processor.calculateStatistics(processedData)
```

- Mix camelCase and snake_case in function and variable names.
- Use inconsistent capitalization in class and method names.
- Combine different naming conventions within the same code block, making it hard to follow a consistent style.

---


# Rule #5: Magic Numbers


```python
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

```

- Use numbers like 42, 17, 23, 13, 3.14, 2.718 without any explanation.
- Integrate these magic numbers into complex calculations. Why use constants when you can keep them mystified?

---


# Interactive Break: Spot the Obfuscation


Can you find the confusing elements in this code snippet?

```python
def enigmatic_transformation(input_str):
    def __hidden_transmutation(s, magic_number=0x42):
        return ''.join([chr(ord(c) ^ magic_number) for c in s])

    encrypted_str = __hidden_transmutation(input_str)
    transformed_encrypted = encrypted_str[::-1]
    final_output = __hidden_transmutation(transformed_encrypted)
    return final_output

result = enigmatic_transformation("Hello World!")
```

^

- Examine the private nested function applying bitwise operations.
- Focus on how the string undergoes transformation and then another operation.

---

Well, it's not that hard to figure out what this code does, but it's still confusing enough to make you wonder why it's written this way.

The complexity disguises a simple yet common string operation.

```python
result = input_str[::-1]
```

---

# Rule #6: Overcomplicate Simple Tasks


```python
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
```

- Why make it simple when we can use recursion for a simple even-odd check
- Bonus points for embeding the logic within private helper functions to further complicate the understanding.
 
---

# Rule #7: Commenting Out Code


```python
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
```

- Never delete old code, just comment it out.
- It's like an archeological dig for future coders!
- Mix actual code with large commented sections to obscure the current functionality.

---


# Rule #8: Misleading Comments


```python
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

# Example usage
result = deceptive_function([4, 1, 3, 2, 2, 5])
```

- Comments should seldom match the code's purpose.
- Confuse and conquer!

---


# Rule #9: Redundant Code


```python
def is_positive(number):
    if number > 0:
        return True
    else:
        return True
```

- Redundancy is key.
- Let them ponder the purpose of your code.

---


# Rule #10: Creative Use of Data Types


```python
def type_confusion_mixer(input_data):
    # Convert input to a string, regardless of type
    stringified_data = str(input_data)

    # Perform arithmetic on string characters
    numerical_transform = [ord(char) + 5 for char in stringified_data]

    # Create a dictionary from the numerical list
    data_dict = dict(enumerate(numerical_transform))

    # Convert dictionary to a list of tuples, then to a string
    tuple_list = list(data_dict.items())
    tuple_string = str(tuple_list)

    # Final output: Boolean based on arbitrary condition
    return tuple_string == stringified_data[::-1]

result = type_confusion_mixer([1, 2, 3, 'a', 'b', 'c'])
```

- Data types? Just a suggestion.
- Mix and match for maximum confusion.

---


# Interactive Quiz


What does this function do?

```python
def mystery(x):
    return [ord(c) for c in x]
```

1. Converts a string to a list of ASCII values.
2. Reverses a string.
3. Checks if a string is a palindrome.

---


# Rule #11: Unnecessary Complexity


```python
def complex_logic():
    try:
        # Complicated logic here
        pass
    except Exception as e:
        raise e
```

- Wrap everything in `try-except`.
- Even when it's not needed.

---


# Rule #12: Arbitrary Restrictions


```python
def print_numbers(limit):
    for i in range(1, limit):
        if i == 4:
            continue
        print(i)
```

- Introduce random restrictions.
- Make them wonder why `4` is so special.

---


# Rule #13: Cryptic Algorithms


```python
def cryptic_algo(a, b):
    return a * b - a / b + a % b
```

- The more cryptic, the better.
- Make simple algorithms look complex.

---


# Rule #14: Repetitive Code


```python
def check_status():
    if status == "active":
        return True
    if status == "inactive":
        return False
```

- Don't use `elif` or `switch`.
- Repetition is your ally.

---


# Rule #15: Misuse of Global Variables


```python
global_variable = 0

def misuse_globals():
    global global_variable
    global_variable += 1
```

- Abuse global variables.
- They should be in every method!

---

# Rule #16: Misuse of Language

```python
def procesarDatos(datos):
    # Processing data...
    pass
```

- Mix languages in your code.
- Use variable names from different languages for an international flair.

---

# Rule #17: Complex Logic in Simple Functions

```python
def simpleTask():
    # Complex logic that seems unnecessary
    pass
```

- Overcomplicate tasks that should be simple.
- Make simple functions look like they solve world hunger.

---

# Rule #18: Arbitrary Code Formatting

```python
def oddlyFormattedFunction():
 return True
```

- Use inconsistent indentations and spacing.
- The more erratic, the better.

---

# Rule #19: Useless Comments

```python
# This function does something
def doSomething():
    pass
```

- Add comments that state the obvious, or better yet, the irrelevant.
- Keep them guessing the actual purpose.

---

# Rule #20: Redefine Standard Functions

```python
import math
def sqrt(x):
    return x ** 2
```

- Redefine standard library functions incorrectly.
- Create a parallel universe where nothing works as expected.

---

# Rule #21: Overuse Design Patterns

```python
# Implement every design pattern possible, even if unnecessary
class AbstractFactorySingletonProxy:
    pass
```

- Implement design patterns where they aren't needed.
- The more complex, the better.

---

# Rule #22: Unnecessary Recursion

```python
def recursiveConfusion(n):
    if n > 0:
        return recursiveConfusion(n-1)
    return "confusion"
```

- Use recursion for tasks easily done with loops.
- Turn simple tasks into a labyrinth of recursive calls.

---

# Rule #23: Misleading Function Names

```python
def deleteAllFiles():
    # Function actually creates files
    pass
```

- Name functions the opposite of what they do.
- Lead others on a wild goose chase.

---

# Rule #24: Abusing Global Variables

```python
global chaos
chaos = 42

def wreakHavoc():
    global chaos
    chaos += 1
```

- Use and modify global variables recklessly.
- Watch as everyone tries to untangle the web of dependencies.

---

# Rule #25: Bizarre Error Handling

```python
try:
    # Risky operation
    pass
except:
    print("Something happened, but I won't tell you what")
```

- Use vague error messages.
- Catch all exceptions and handle them all the same way: poorly.

---



# Closing Thoughts


- Writing unmaintainable code is an art form.
- Today, you've taken your first steps to mastering this craft.
- Go forth and code (confusingly)!

---

-> Q/A <-

-> Go on! Ask me some spicy questions? <- 

---


-> # Thank You! <-


-> █▀▀▀▀▀█  ▄▄▀▀▄█ ▄ █▀▀▀▀▀█  <-
-> █ ███ █ ▄   █▄ █▄ █ ███ █  <-
-> █ ▀▀▀ █ ▀▀ ▄▄█  ▀ █ ▀▀▀ █  <-
-> ▀▀▀▀▀▀▀ ▀ █▄▀ █ █ ▀▀▀▀▀▀▀  <-
-> █▀▄ ▄█▀▀ █ ▀▄▀▀█▀  ▄██▄▄   <-
-> ▀▄███▀▀█▀▄▀ ▄▀ ▀▀▄▀▄██ ▀█  <-
-> █▄▄█▄▀▀ ▀▀ ▀▀▄ ██ ▀▀   ▄▀  <-
-> █  █▀▀▀▀  ▄█▀ ▀█▄█   ▀▄▀█  <-
-> ▀ ▀▀ ▀▀▀█▀█▀█▀▀ █▀▀▀█ █    <-
-> █▀▀▀▀▀█ █▀ █▄▀█▄█ ▀ █▀ ▄█  <-
-> █ ███ █  █ █▀███▀███▀█▀▄▄  <-
-> █ ▀▀▀ █ ▄▀█ ▄ ▀ █▄ █▄ ▀ █  <-
-> ▀▀▀▀▀▀▀ ▀   ▀  ▀▀ ▀  ▀  ▀  <-
