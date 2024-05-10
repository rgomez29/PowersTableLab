# Powers Table (Loops)
print("Learn your squares and cubes!")


# Store user values
user_input = int(input(f"Please enter an integer!"))
print(user_input)

# Use user input to calculate values in each column
def create_table(user_input):
    numbers = []
    squares = []
    cubes = []
    for i in range(1, user_input + 1):
        numbers.append(i)
        squares.append(i ** 2)
        cubes.append(i ** 3)
    return numbers, squares, cubes

# Print table with a numbers column, squared column, and cubed column
def print_table(numbers, squares, cubes):
    print("Numbers\tSquares\tCubes")
    for i in range(len(numbers)):
        print(f"{numbers[i]}\t{squares[i]}\t{cubes[i]}")

# Store final values/output
numbers, squares, cubes = create_table(user_input)
print_table(numbers, squares, cubes)