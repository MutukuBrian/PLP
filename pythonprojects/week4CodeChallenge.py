# Step 1: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Count the number of words
word_count = len(content.split())

# Step 3: Convert text to uppercase
uppercase_content = content.upper()

# Step 4: Write processed text and word count to output.txt
with open("output.txt", "w") as output_file:
    output_file.write(uppercase_content + "\n")
    output_file.write(f"\nWord Count: {word_count}")

# Step 5: Print success message
print("✅ Processing complete! Data has been written to output.txt.")