# Accept user input to create a list of integers
numbers = input("Enter numbers separated by spaces: ").split()

# Convert input strings to integers
numbers = [int(num) for num in numbers]

total_sum = sum(numbers)

print(f"The sum of the entered numbers is: {total_sum}")