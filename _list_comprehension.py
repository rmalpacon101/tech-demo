# Traditional for loop
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]

# With conditional filtering
even_squares = [x**2 for x in range(10) if x % 2 == 0]

dict_squares = {x: x**2 for x in range(10)}
set_squares = {x**2 for x in range(10)}
tuple_squares = tuple(x**2 for x in range(10))