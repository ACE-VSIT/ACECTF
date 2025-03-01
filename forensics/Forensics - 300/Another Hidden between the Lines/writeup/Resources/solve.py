def decode_hidden_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    
    binary_data = []
    i = 0
    while i < len(content):
        if content[i] == 10:  # Linux line ending: \n
            binary_data.append('0')
            i += 1
        elif content[i] == 13 and i + 1 < len(content) and content[i + 1] == 10:  # Windows line ending: \r\n
            binary_data.append('1')
            i += 2  # Skip the \r and \n
        else:
            i += 1  # Skip any non-line-ending byte (if present)

    # Join the binary data and split into 8-bit chunks
    binary_str = ''.join(binary_data)
    ascii_text = ''.join(chr(int(binary_str[i:i + 8], 2)) for i in range(0, len(binary_str), 8))

    return ascii_text

# Path to the file 'hidden'
file_path = 'hidden'
flag = decode_hidden_file(file_path)
print(flag)
