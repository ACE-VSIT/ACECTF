## **Challenge Name: Super Secure Encryption**

### **Solves**
- **Solves**: 362
- **Points**: 100

### **Description**

I'm doing a big favour with this one... I'm handing out my super secure functionality to the outer world to stumble upon & explore.
Though, I still remember one of my colleagues once saying that nothing in this world is secure nowadays but my script right here stands on the contrary. I'll give you the access to my arsenal and see if you can prove me wrong.

**Attachments**

- [chall.py](../challenge-files/chall.py)
- [msg.txt](../challenge-files/msg.txt)

---

### **Approach**

## **Solution**

To break the encryption and retrieve the flag, follow these steps:

### **1. Understanding the Encryption**
- The script uses **AES in CTR mode**, which is **vulnerable to key reuse**.
- The same **random key (`k`) and counter** are used for encrypting both a **test message** and the **flag**.
- Since AES-CTR acts as a **stream cipher**, XORing two ciphertexts allows us to recover the plaintext.

### **2. Exploiting Key Reuse**
- Given two ciphertexts (`encrypted_message` and `encrypted_flag`), we can **XOR** them together to eliminate the key stream.
- Since we know the plaintext of `encrypted_message` (test message), we can XOR it back to recover the flag.

### **3. Solution Script**
```python
import binascii
from pwn import xor

with open("msg.txt") as h:
    encrypted_message = binascii.unhexlify(h.readline().strip())
    encrypted_flag = binascii.unhexlify(h.readline().strip())

test = b'This is just a test message and can totally be ignored.'

xor_1 = xor(encrypted_message,encrypted_flag)
xor_2 = xor(xor_1,test)

flag = xor_2[:len(encrypted_flag)]

print(f"{flag=}")
```

### **4. Explanation**
1. **Read the encrypted test message and flag** from `msg.txt`.
2. **XOR the two encrypted texts** to remove the key stream.
3. **XOR the result with the known plaintext** to extract the flag.

Decryption script - [solve.py](Resources/solve.py)

### **Flag**
```
ACECTF{n07h1n6_15_53cur3_1n_7h15_w0rld}
```

---