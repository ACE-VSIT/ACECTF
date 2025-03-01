## **Challenge Name: Cryptic Pixels**

### **Solves**
- **Solves**: - 206
- **Points**: 200 

### **Description**
This image looks normal at first, but something important is hidden inside. The secret is carefully concealed, making it hard to find.

Your task is to explore the image, uncover the hidden message, and reveal what’s concealed.Do you have what it takes to crack the code and unlock the secret?

### **Approach**

1. Use **binwalk** to analyze the image and identify hidden data [Binwalk](Resources/1.png)

2. Extracting the hidden ZIP file from the image using **binwalk** [Binwalk Extraction](Resources/2.png) [Image Content](Resources/3.png)

3. Use **zip2john** to create a password hash [Password Hash](Resources/4.png)

4. Use **John the Ripper** to crack the password [Password Cracking](Resources/5.png)

5. Unzipping the ZIP file using the extracted password [File Unzipping](Resources/6.png)

6. Decoding the **Caesar Cipher** encoded flag to get the final flag [Flag](Resources/7.png)

### **Flag**
```
ACECTF{h4h4_y0u'r3_5m4r7}
```
