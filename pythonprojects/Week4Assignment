def process_file():
    # Prompt user for the input filename
    filename = input("Enter the filename to read: ")
    
    try:
        # open the file for reading
        with open(filename, "r") as file:
            content = file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Write modified content to a new file
        output_filename = "modified_" + filename
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)
        
        print(f"✅ Processing complete! Modified content saved to {output_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found. Please enter a valid filename.")
    except IOError:
        print("❌ Error: Unable to read the file. Check permissions or file format.")

# Run the function
process_file()