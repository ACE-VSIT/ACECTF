## **Challenge Name: Virtual Hard Disk**

### **Solves**
- **Solves**: 98
- **Points**: 200  

### **Description**
One of the first things I learnt when I started learning to hack was linux.
It was fun until I hit a ceiling of understanding about the differences in Operating Systems, what's a Shell, Kernel, etc.

But once I got better I started developing a liking towards the terminal and how the Linux operating system is `better` than say Windows, or `worse` in some cases.
How none of them is superior, nor the other inferior. We shall find out with this challenge.

Be careful, a lot of fake galfs around.

**Attachments**

- [challenge](https://drive.google.com/file/d/1tZv94aEKV4Mc33sJECWVqqAEPiXHhCd-/view)

---

### **Approach**

#### **1. Identifying the File Type**  
- The challenge title, **Virtual Hard Disk**, hints at a **.vhd** file.  
- Running the `file` command confirms this:  

```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ file challenge                      
challenge: DOS/MBR boot sector MS-MBR Windows 7 English at offset 0x163 "Invalid partition table" at offset 0x17b "Error loading operating system" at offset 0x19a "Missing operating system" end-CHS (0xb,254,63), startsector 1, 4294967295 sectors
```

- This indicates that the file is a **Windows Virtual Hard Disk (VHD)**.  

---

### **2. Extracting the VHD Contents**  

#### **On Linux**  

1. **Install Required Tools**  
   ```bash
   sudo apt update
   sudo apt install qemu-utils parted ntfs-3g
   ```

2. **Mount the VHD Using qemu-nbd**  
   ```bash
   sudo modprobe nbd
   sudo qemu-nbd -c /dev/nbd0 /home/kali/Desktop/challenge.vhd
   ```

3. **Identify Partitions**  
   ```bash
   sudo parted /dev/nbd0 print
   ```

4. **Mount the Partition**  
   ```bash
   sudo mkdir -p /mnt/chal
   sudo mount -t ntfs-3g /dev/nbd0p1 /mnt/chal
   cd /mnt/chal
   ```

5. **Handling Alternate Data Streams (ADS)**  
   - Linux does not support **ADS**, so we need to use `sleuthkit`:  

   ```bash
   sudo fls -r -m / /dev/nbd0p1
   ```

   - The output lists the **ADS entries**:  

   ```
   666c61672e747874.jpg:Flag
   666c61672e747874.jpg:Key
   ```

6. **Extract the Flag and Key**  
   ```bash
   sudo icat /dev/nbd0p1 49-128-3 > extracted_flag.txt
   sudo icat /dev/nbd0p1 49-132-3 > extracted_key.txt  
   ```

7. **Print the Extracted Files**  
   ```bash
   cat extracted_flag.txt
   ```

   ```
   CTCHHW{7t3_h1hw3p3sq3_s37i33r_a0l_4li_a3}
   ```

   ```bash
   cat extracted_key.txt
   ```

   ```
   Key='cryforme'
   ```

---

#### **On Windows**  

1. **Rename the File for Disk Management Compatibility**  
   - Rename `challenge` to `challenge.vhd`.  

2. **Attach the VHD**  
   - Open **Disk Management** (`Win + X → Disk Management`).  
   - Click **Action → Attach VHD**.  
   - Select `challenge.vhd`.  
   - A new volume will appear.  

3. **List Alternate Data Streams**  

   ```cmd
   dir /R
   ```

   Output:  
   ```
   666c61672e747874.jpg:Flag:$DATA
   666c61672e747874.jpg:Key:$DATA
   ```

4. **Extract the Key and Flag Using PowerShell**  

   ```powershell
   PS I:\> Get-Content .\666c61672e747874.jpg -Stream Key
   ```

   ```
   Key='cryforme'
   ```

   ```powershell
   PS I:\> Get-Content .\666c61672e747874.jpg -Stream Flag
   ```

   ```
   CTCHHW{7t3_h1hw3p3sq3_s37i33r_a0l_4li_a3}
   ```

   OR using Command Prompt:  

   ```cmd
   more < "I:\666c61672e747874.jpg:Flag"
   ```

   ```
   CTCHHW{7t3_h1hw3p3sq3_s37i33r_a0l_4li_a3}
   ```

   ```cmd
   more < "I:\666c61672e747874.jpg:Key"
   ```

   ```
   Key='cryforme'
   ```

---

### **3. Decrypting the Flag**  
- The extracted **flag** is encrypted using **Vigenère cipher** with the key **"cryforme"**.  
- Decrypting it gives:  

```plaintext
ACECTF{7h3_d1ff3r3nc3_b37w33n_y0u_4nd_m3}
```

---

### **Flag**
```
ACECTF{7h3_d1ff3r3nc3_b37w33n_y0u_4nd_m3}
```
---
