# Traditional loop
squares = []
for x in range(5):
    squares.append(x**2)

print(f"Traditional list: ",squares)

# List comprehension
squares = [x**2 for x in range(5)]
print(f"List comprehension: ",squares)  # Output: [0, 1, 4, 9, 16]



#Transforming Data:

names = ["Alice", "Bob", "Charlie"]
uppercased_names = [name.upper() for name in names]
print(uppercased_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']

#Filtering Data:

numbers = [10, 15, 20, 25, 30]
divisible_by_5 = [num for num in numbers if num % 5 == 0]
print(divisible_by_5)  # Output: [10, 15, 20, 25, 30]

#Flattening a List:

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]