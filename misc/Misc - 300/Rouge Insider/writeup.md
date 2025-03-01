# **Challenge Title: Rogue Insider**

## **Challenge Header**
A suspicious activity report hints at a rogue insider hiding critical information deep in the server logs. Your task is to analyze the Linux file system, trace the activity, and recover the hidden flag.

## **Solution Steps**

### **1. Explore the File System**
- Begin by extracting the file and guessing a very easy password by which the file is protected with which is "Kali", then reading the `/etc/motd` file to find the first hint.  
  This will point to the next step in uncovering the rogue insider's trail.

---

### **2. Locate the Logs**
- Navigate to the directory `/var/log/rotated_logs`.  
- Extract the compressed log file `archived.log.1.gz` for analysis.  
gunzip archived.log.1.gz

Analyze its contents for further clues.

---

### **3. Investigate System Logs**
- Head to `/var/log/journal/2296c86330c3408caad86414c8b2e916/system`.  
- Search for log entries labeled **DEBUG** to gather critical data.  

---

### **4. Piece Together the Initial Flag**
- From the **DEBUG** log entries, assemble the partial flag.  
- The initial flag retrieved:  
ACECTF{5y573m_n33d5_r3574r7}

---

### **5. Decrypt the Flag**
The flag is encrypted using **ASCII Mod 10**. Follow the decryption process to retrieve the original flag.

#### **Step-by-Step Decryption**
| Character | ASCII Value | Sum of Digits  | Mod 10 |
| --------- | ----------- | -------------- | ------ |
| 5         | 53          | 5 + 3 = 8      | 8      |
| y         | 121         | 1 + 2 + 1 = 4  | 4      |
| 5         | 53          | 5 + 3 = 8      | 8      |
| 7         | 55          | 5 + 5 = 10     | 0      |
| 3         | 51          | 5 + 1 = 6      | 6      |
| m         | 109         | 1 + 0 + 9 = 10 | 0      |
| _         | 95          | 9 + 5 = 14     | 4      |
| n         | 110         | 1 + 1 + 0 = 2  | 2      |
| 3         | 51          | 5 + 1 = 6      | 6      |
| 3         | 51          | 5 + 1 = 6      | 6      |
| d         | 100         | 1 + 0 + 0 = 1  | 1      |
| 5         | 53          | 5 + 3 = 8      | 8      |
| _         | 95          | 9 + 5 = 14     | 4      |
| r         | 114         | 1 + 1 + 4 = 6  | 6      |
| 3         | 51          | 5 + 1 = 6      | 6      |
| 5         | 53          | 5 + 3 = 8      | 8      |
| 7         | 55          | 5 + 5 = 10     | 0      |
| 4         | 52          | 5 + 2 = 7      | 7      |
| r         | 114         | 1 + 1 + 4 = 6  | 6      |
| 7         | 55          | 5 + 5 = 10     | 0      |

#### **Encrypted Result**
84806 42661 46807 60


#### **Reverse the Encryption**
Using the provided ASCII table located at `/home/Linux/downloads`, reverse the **ASCII Mod 10** process to reveal the original flag:
ACECTF{5y573m_n33d5_r3574r7}


---

## **Hints**
- The file `/home/Linux/downloads` contains the full ASCII table to assist with decryption.  
- Multiple locations in the file system provide subtle nudges toward understanding the **ASCII Mod 10** encryption process.

---

## **Flag**
ACECTF{5y573m_n33d5_r3574r7}
