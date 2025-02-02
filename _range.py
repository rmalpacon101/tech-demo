gen = range(5)

print(type(gen))
# Basic range with stop value
print("\nBasic range with stop value:")
for i in range(5):
    print(i)

# Range with start and stop
print("\nRange with start and stop:")
for i in range(2, 5):
    print(i)

# Range with start, stop, and step
print("\nRange with start, stop, and step:")
for i in range(0, 10, 2):
    print(i)

# Negative step for counting down
print("\nNegative step for counting down:")
for i in range(5, 0, -1):
    print(i)