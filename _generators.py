# 1. Simple number generator
def _number_generator(n: int):
    for i in range(n):
        yield i


# Generator expression
data = (i for i in range(5))
data_tuple = ((i, i) for i in range(5))

print(type(data))

if __name__ == "__main__":
    # 1. Using next() function
    gen = _number_generator(5)

    print(next(gen))
    print(next(gen))
    print("Using next() function")
    print(next(gen))
    print(next(gen))
    print("Using next() function again")
    print("Using next() function expecting None = ", print(next(gen)))
    print("\n")

    # 2. Using the generator in a for loop
    for i in _number_generator(5):
        print("Using for loop = ", i)

    print("\n")

    # 3. Using the generator expression
    for i in data:
        print(i)

    print("\n")
