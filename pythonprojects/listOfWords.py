# List of words
words = ["Python", "Developer", "AI", "Code", "Innovation", "Script", "Tech"]

# Using list comprehension to filter words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Display the result
print(f"Words with an odd number of characters: {odd_length_words}")