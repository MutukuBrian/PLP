# Accept user input and convert it into sets of integers
set1 = set(map(int, input("Enter numbers for the first set (space-separated): ").split()))
set2 = set(map(int, input("Enter numbers for the second set (space-separated): ").split()))

# Find the common elements
common_elements = set1 & set2  # Using the intersection operator "&"

print(f"\nFirst set: {set1}")
print(f"Second set: {set2}")
print(f"Common elements: {common_elements}")