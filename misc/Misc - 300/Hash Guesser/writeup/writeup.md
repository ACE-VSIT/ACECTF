## **Challenge Name: Virtual Hard Disk**  

### **Solves**  
- **Solves**: 41 
- **Points**: 300  

### **Description**  
Welcome to the only cracking challenge of ACECTF1.0, here we have a Hash that we need to crack. The target hash has been taken from a very famous wordlist which has around what 14 million passwords? Yeah, but it's not that simple, the target hash has been `base32 encoded` & then `reversed` before generating the `MD5 hash`. I guess that's enough information for you to start, good luck.

**Connect to the challenge:**  
```bash
nc 34.131.133.224 5000
```

### **Attachments**  
- [script.py](../challenge-files/script.py)  

---

## **Approach**  

To solve this challenge, we have two possible approaches:  

### **Method 1 (Brute Force - Slow & Tedious)**  
- Read the `rockyou.txt` wordlist locally.  
- **Base32 encode** each password.  
- **Reverse** the encoded string.  
- **Generate the MD5 hash** of the reversed string.  
- Send it to the server to check if it matches.  

However, this method is inefficient because it requires hashing **millions of passwords**.

### **Method 2 (Efficient - Using Server Feedback)**  
We can optimize the process using a more intelligent approach:

1. **Read passwords from `rockyou.txt` (or any wordlist).**  
2. **Apply transformations:**  
   - **Base32 encode** the password.  
   - **Reverse** the encoded string.  
   - **Generate the MD5 hash** of the reversed string.  
3. **Use server feedback to identify missing hex characters:**  
   - The server provides feedback on how many characters match the correct hash.  
   - If a hash is missing at least one **hex character** (`0-9, a-f`), it becomes a strong candidate.  
4. **Print the potential password and its hash when a mismatch is detected.**  
5. **Submit the correct hash to retrieve the flag.**  

Using this method significantly reduces the number of passwords we need to check, making it much more efficient.

Use [solve.py](Resources/solve.py)

---

### **Flag**
```
ACECTF{h45h_cr4ck1n6_r3qu1r35_4_l177l3_w17}
```
---