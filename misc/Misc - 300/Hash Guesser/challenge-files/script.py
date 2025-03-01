import hashlib
import base64

wordlist = "WORDLIST.TXT"

def process_passwords(file_path):
    with open(file_path, "r", encoding="latin-1") as file:
        for line_number, password in enumerate(file, start=1):
            
            password = password.strip()
            
            # Convert to base32
            b32_encoded = base64.b32encode(password.encode()).decode()
            
            # Reverse it
            reversed_b32 = b32_encoded[::-1]
            
            # Generate MD5 hash
            md5_hash = hashlib.md5(reversed_b32.encode()).hexdigest()
            
            # Check if hash is missing any hex characters
            for char in "0123456789abcdef":
                if char not in md5_hash:
                    print(f"Password: {password}")
                    print(f"MD5 Hash: {md5_hash}")
                    print(f"Missing Character: {char}")
                    return

if __name__ == "__main__":
    process_passwords(wordlist)
