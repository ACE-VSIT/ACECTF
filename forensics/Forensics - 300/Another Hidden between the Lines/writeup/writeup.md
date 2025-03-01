## **Challenge Name: Another Hidden between the Lines?**

### **Solves**
- **Solves**: 54
- **Points**: 300 

### **Description**

**Question**: Is this another one of those hidden in plain sight typical normie challenges?  
**Answer**: No.

This challenge is very simple. You have a file named **hidden**, and all you need to do is retrieve the flag. My focus for this year's CTF is not just the beginning but also ending on a high note. I won't rely on overused "read between the lines" challenges; instead, I want you to do some research.  

**Good Luck!**

### **Attachments**
- [hidden](../challenge-files/hidden)

---

## **Approach**

This is a forensic challenge where we have a text file named `hidden`. Opening the file, we see that it appears completely empty. However, it is not whitespace steganography like typical CTF challenges. Instead, this challenge makes use of **LF (Line Feed) and CRLF (Carriage Return Line Feed).**

### **Understanding the Concept**
- **Linux uses `\n` (LF) to mark the end of a line.**
- **Windows uses `\r\n` (CRLF) for line endings.**
- When viewed in a text editor, both appear as blank spaces, which makes it interesting.

The key observation here is:
- **LF (`\n`) represents 0**
- **CRLF (`\r\n`) represents 1**

Reconstructing these into a binary sequence and converting to ASCII gives the flag.

---

### **Solution Walkthrough**

#### **Step 1: Analyzing the File**
Running the `file` command on the `hidden` file provides our first hint:
```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ file hidden
hidden: ASCII text, with CRLF, LF line terminators
```

This confirms that the file contains a mix of **CRLF and LF** line endings.

#### **Step 2: Viewing the Line Endings**
Using `cat -A` to display special characters:
```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ cat -A hidden
$  
^M$  
$  
$  
$  
$  
^M$  
$  
^M$  
$  
$  
$  
```
Here, we notice a pattern:
- **`$` (LF)** represents `0`
- **`^M$` (CRLF)** represents `1`

This confirms that the file contains **binary-encoded data** using newline characters.

---

### **Extracting the Flag**
To automate the extraction, we can use a script to:
1. Read the file line by line.
2. Identify `\n` (LF) as `0` and `\r\n` (CRLF) as `1`.
3. Convert the binary string to ASCII text.

Use [script.sh](Resources/script.sh) or [solve.py](Resources/solve.py) to automate it and extract the binary values convert to plaintext and print it out.

---

### **Flag**
```
ACECTF{n0_r34d1n6_be7w33n_7h3_l1n35}
```
---

