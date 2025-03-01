## **Challenge Name: Tabs$sapces**

### **Solves**
- **Solves**: 141
- **Points**: 100  

### **Description**
A mysterious ZIP file containing a collection of images and a file has been discovered.The task is to retrieve the flag.
---

### **Attachments**

- [Tabs&spaces.zip](../challenge-files/Tabs&spaces.zip)

---

### **Approach**

1. **Extract the Files**
    - Unzip the provided ZIP file using the `unzip` command:
      ```bash
      unzip <filename>.zip
      ```
    - The ZIP file contains:
      - A file named with a alpha-number value.
      - A folder with approximately 100 image files.

2. **Analyze the Number-Named File**
    - Open the file in a text editor or use the `cat` command:
      ```bash
      cat <filename>
      ```
    - Upon inspection, you will find that the wierd numbered file is a Python script that compares the checksum of each image in the folder and identifies the correct one based on its checksum, and you will come to notice that the name of the script is the checksum of the targetted file so you will copy that checksum to the script and it will show you the image containing the flag.
    - or an alternative would be that the size of the real flag image is less then all the other fake flag images

3. **Run the Python Script**
    - Make the script executable:
      ```bash
      chmod +x <filename>
      ```
    - Execute the script with:
      ```bash
      python3 <filename>
      ```
    - The script will output the name of the real image file.

4. **Inspect the Real Image**
    - Once the real image is identified, open it using the steghide
      ```bash
      steghide extract -sf real_imagename.jpg
      ```
    - this will genetrate a output file containing tabs and spaces

5. **Decode the Tabs and Spaces**
    - Convert tabs and spaces into binary:
      - Tabs (`\t`) represent `1`.
      - Spaces (` `) represent `0`.
    - Use a Python script or manually convert the binary sequence into text.

6. **Convert Binary to Text**
    - Once you have the binary string, convert it into text using an online binary-to-text converter or a simple Python script.
    - The decoded message will reveal the hidden flag

---

### **Flag**
```
ACECTF{n0_3xp1017_n0_g41n}
```

---