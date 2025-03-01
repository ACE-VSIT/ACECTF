def reverse_file(input_file, output_file):
    # Open the input file in binary read mode
    with open(input_file, 'rb') as f:
        # Read the file contents
        file_data = f.read()

    # Reverse the file data
    reversed_data = file_data[::-1]

    # Write the reversed data to the output file
    with open(output_file, 'wb') as f:
        f.write(reversed_data)

    print(f"Reversed binary data saved to {output_file}")

# Input and output file names
input_file = "Reverseme.png"  # Change this to your input file path
output_file = "reverse_me"

# Call the function
reverse_file(input_file, output_file)
