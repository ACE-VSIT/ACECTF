import base64
import hashlib
import time
import multiprocessing
from pwn import remote

HOST, PORT = "34.131.133.224", 5000

def request(md5_hash):
    """Sends an MD5 hash to the server and retrieves feedback."""
    try:
        with remote(HOST, PORT) as p:
            p.sendlineafter(b"Enter MD5 hash: ", md5_hash)
            response = p.recvline().strip().decode()
            
            if "Characters matched" in response:
                num_occurrences = int(response.split(": ")[1].split("/")[0])
                if num_occurrences == 32:
                    p.recvuntil(b"Flag: ")
                    flag = p.recvline().strip().decode()
                    return num_occurrences, flag
            return num_occurrences, ""
    except Exception as e:
        print(f"[ERROR] {e}")
        return 0, ""

def get_histogram():
    """Determines the character frequency of the target MD5 hash."""
    histogram = [0] * 16
    hex_chars = "0123456789abcdef"
    
    for i, char in enumerate(hex_chars):
        print(f"Checking character {char} ({i+1}/16)")
        num, _ = request((char * 32).encode())
        histogram[i] = num
    
    print("[INFO] Histogram built:", histogram)
    return histogram

def hash_matches_histogram(md5_hash, histogram):
    """Checks if an MD5 hash has the same character distribution as the target histogram."""
    temp = [0] * 16
    for c in md5_hash:
        index = int(c, 16)  # Convert hex character to index
        temp[index] += 1
    return temp == histogram

def process_wordlist(histogram, flag_found, start_line=0, end_line=None):
    """Brute-force search for the correct password using the wordlist."""
    with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as file:
        for line_number, password in enumerate(file, start=1):
            if flag_found.value:  # Stop if another process found the flag
                return

            if line_number < start_line:
                continue
            if end_line and line_number > end_line:
                break

            password = password.strip()
            b32_encoded = base64.b32encode(password.encode()).decode()
            reversed_b32 = b32_encoded[::-1]
            md5_hash = hashlib.md5(reversed_b32.encode()).hexdigest()

            if hash_matches_histogram(md5_hash, histogram):
                _, flag = request(md5_hash.encode())
                if flag:
                    print(f"[SUCCESS] Flag found: {flag}")
                    flag_found.value = 1  # Signal all processes to stop
                    return

            if line_number % 1000 == 0:
                print(f"[INFO] Processed {line_number} passwords...")

def main():
    print("[INFO] Building histogram...")
    histogram = get_histogram()

    print("[INFO] Starting brute-force search...")
    num_cores = multiprocessing.cpu_count()
    chunk_size = 50000  # Define a range of lines per process
    jobs = []
    
    with multiprocessing.Manager() as manager:
        flag_found = manager.Value("i", 0)  # Shared variable to stop all processes
        
        for i in range(num_cores):
            start_line = i * chunk_size + 1
            end_line = (i + 1) * chunk_size
            p = multiprocessing.Process(target=process_wordlist, args=(histogram, flag_found, start_line, end_line))
            jobs.append(p)
            p.start()

        for job in jobs:
            job.join()
    
    print("[INFO] Brute-force search completed.")

if __name__ == "__main__":
    main()