## **Challenge Name: Deep Memory Dive**

### **Solves**
- **Solves**: 39
- **Points**: 400 

### **Description**

A gamer was experiencing severe lag while playing. They decided to disable unnecessary startup applications to free up system resources. However, after investigating the system, they noticed an unusual entry in the Startup registry.

The flag is divided in different parts. Investigate the dump and gather all the flags.

Flag Format: ACECTF{3x4mpl3_fl4g}

**Attachments**
Memory Dump file: https://drive.google.com/file/d/1KpikCPZyV8u1iWUiGE7xjsm3uKSAVd9b/view?usp=drive_link

### **Approach**

1.  Extracting the Flag from the Windows Registry

**Volatility 3 Plugin to Use:**
- `windows.registry.printkey`

**Command:**
```bash
vol -f memdump.raw windows.registry.hivelist
```
*This lists all available registry hives in the memory dump.*

Once you identify the hive where the flag might be stored, use:
```bash
vol -f memdump.raw windows.registry.printkey --key "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
```

**Expected Output:**
```
Key: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Value: ACECTF{3xplor1n6_
```

---

2. Extracting the Flag from Clipboard Data

**Volatility 3 Plugin to Use:**
- `windows.clipboard`

**Command:**
```bash
vol -f memdump.raw windows.clipboard
```

**Expected Output:**
```
Clipboard Data:
th3_
```

---

3. Extracting the Flag from CMD History

**Volatility 3 Plugin to Use:**
- `windows.cmdscan`

**Command:**
```bash
vol -f memdump.raw windows.cmdscan
```

**Expected Output:**
```
0x12345678: echo flag c0nc3al3d_
```

---

4. Extracting the Flag from a Running Process

**Volatility 3 Plugins to Use:**
- `windows.pslist`

**Identify Running Processes**
```bash
vol -f memdump.raw windows.pslist
```

**Expected Output (Look for a suspicious process):**
```
PID   Process Name
----  ------------
1234  last_part_is_{r1ddl3s}.exe
```

---

5. Reconstructing the Final Flag
Once all parts are collected, we can reconstruct the complete flag:

1. **Windows Registry**: `ACECTF{3xplor1n6_`
2. **Clipboard Data**: `th3_`
3. **CMD Echo History**: `c0nc3al3d_`
4. **Process Memory (Running Process)**: `last_part_is_{r1ddl3s}.exe`

## **Flag**

```
ACECTF{3xplor1n6_th3_c0nc3al3d_r1ddl3s}
```
## **Author**

Navii

---


