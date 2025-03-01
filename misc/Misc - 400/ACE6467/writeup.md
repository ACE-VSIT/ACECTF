# **Challenge Title: ACE6467**

### Solves: **

- **Solves: 2**
- **Points: 400**

## **Description**
A challenging task that combines steganography and cryptography techniques to uncover a hidden flag. Participants must analyze images, extract hidden metadata, and decode multiple layers of encryption to find the flag.

## **Approach**

### **Step 1: Extract Metadata Hints**
- Analyze the provided image for hidden clues using tools like **ExifTool**:  
  ```bash
  exiftool <image_name>
  ```
- Discover the hint:  
  ```
  "heightxwidth+?"
  ```
  This suggests multiplying the image's dimensions (height × width) and adding a secret number: **6467**.

---

### **Step 2: Calculate the Decryption Key**
- Perform the calculation:  
  ```bash
  height × width + 6467
  ```
- Example: If the image's dimensions are **1024x768**:  
  ```
  (1024 × 768) + 6467 = 2529979
  ```
- This result, **2529979**, is the key to decrypt the image using **Steghide**.

---

### **Step 3: Reveal the First Layer of Information**
- Use **Steghide** to extract a hidden file:  
  ```bash
  steghide extract -sf <image_name> -p 2529979
  ```
- This will reveal a file named `message.txt`.

---

### **Step 4: Decrypt Cryptic Text**
- Open `message.txt`, which contains:
  - Encrypted text (using a **Caesar Cipher with a shift of 7**).
  - A link to a resource (e.g., **Google Drive** or another location).  
- Decode the Caesar Cipher text to uncover instructions and follow the link to retrieve another image.

---

### **Step 5: Unlock the Second Image**
- Analyze the new image's dimensions, e.g., **259x194**.  
- Use the dimensions as the password (raw format: **"259x194"**) to unlock the image:  
  ```bash
  steghide extract -sf <new_image_name> -p "259x194"
  ```
- Extract a file named `Password.txt`.

---

### **Step 6: Decrypt Vigenère Cipher**
- Open `Password.txt`, which contains cryptic text encrypted using a **Vigenère Cipher**.
- Extract the decryption key from the metadata of the second image:
  - Metadata contains a binary string:  
    ```
    01001000 01100001 01101000 01100001 01001011 01100101 01100101 01110000 01010100 01110010 01111001 01101001 01101110 01100111
    ```
  - Convert the binary string to text using a binary-to-text converter:  
    ```
    HahaKeepTrying
    ```
  - This is the decryption key.

---

### **Step 7: Uncover the Final Link**
- Decrypt `Password.txt` using the **Vigenère Cipher** and the key `HahaKeepTrying`.  
- Extract a link to a **GitHub repository**:  
  ```
  https://github.com/oneshhh/book
  ```

---

### **Step 8: Locate the Flag**
- Access the repository and locate the hidden flag on **page 69** of the book.
"The" "B00K" and "Of S3cr3ts."

---

## **Flag**
ACECTF{7h3_b00k_0f_53cr375}