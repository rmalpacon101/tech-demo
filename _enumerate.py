fruits = ['apple', 'banana', 'cherry']

# Without enumerate
print("\nWithout enumerate:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate
print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# With custom start index
print("\nWith custom start index:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Output:
# 1: apple
# 2: banana
# 3: cherry