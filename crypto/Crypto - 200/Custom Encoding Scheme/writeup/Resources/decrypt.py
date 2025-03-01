def extract_flag_bits(output_file):
    # Base64 character set
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Read the encoded output from the file
    with open(output_file, "r") as f:
        encoded_lines = [line.strip() for line in f.readlines()]
    
    # Binary string to hold the extracted bits
    extracted_bits = ""
    
    # Process the first 42 characters (since that's where flag data is embedded)
    for r in encoded_lines[:42]:  # Only process the first 42 lines
        # Decode the Base64 indices
        g = t1.index(r[1])
        d = f"{g:06b}"  # 6 bits for the second Base64 character
        
        # Extract the last 4 bits of `d` (where the flag data is embedded)
        flag_bits = d[-4:]  # The last 4 bits are the embedded flag bits
        extracted_bits += flag_bits  # Append to the binary stream
    
    # Convert the binary stream to ASCII text
    flag = "".join(chr(int(extracted_bits[i:i+8], 2)) for i in range(0, len(extracted_bits), 8))
    
    return flag

output_file = "output.txt"

try:
    extracted_flag = extract_flag_bits(output_file)
    print("Extracted Flag:", extracted_flag)
except Exception as e:
    print("Error:", str(e))
