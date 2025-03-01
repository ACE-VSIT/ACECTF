## **Challenge Name: Keyboard Echo**

### **Solves**
- **Solves**: 85
- **Points**: 300 

### **Description**
You have intercepted USB traffic from a device and captured the data in a .pcapng file. However, the keystrokes are encoded and need to be converted into readable text.

Your task is to analyze the provided packet capture, extract the keystrokes, and reconstruct the original input.

Flag Format: ACECTF{3x4mpl3_fl4g}

### **Approach**

1. **Opening the PCAP File in Wireshark**

Open the provided `.pcapng` file in **Wireshark**.

Apply the following filter to isolate USB HID data:
   ```
   usb.capdata
   ```

Look for **Leftover Capture Data** fields in USB Keyboard packets.

2. **Extracting Keystrokes**

Each **Leftover Capture Data** field contains an 8-byte sequence. This represents the key pressed.

Example:
```
00001c0000000000
```
- The keycode here is `0x1C` (Decimal 28).
- According to the **USB HID Keyboard Usage Table**, `0x1C` corresponds to the letter **'y'**.

By extracting all keycodes, we obtain a sequence of characters.

3. **Decoding Keycodes to Text**
Extracted keycodes and their respective characters:
| Keycode (Hex) | Decimal | Character |
|--------------|---------|-----------|
| 1C          | 28      | y         |
| 27          | 39      | 0         |
| 18          | 24      | u         |
| 0B          | 11      | h         |
| 21          | 33      | 4         |
| 19          | 25      | v         |
| 20          | 32      | 3         |
| 09          | 9       | f         |
| 27          | 39      | 0         |
| 18          | 24      | u         |
| 11          | 17      | n         |
| 07          | 7       | d         |
| 1E          | 30      | 1         |
| 24          | 36      | 7         |

4. **Retrieving the Flag**

The extracted sequence forms the following string:
```
y0uh4v3f0und17
```
Now apply the flag format and add underscores in relevant places.

### **Flag**

```
ACECTF{y0u_h4v3_f0und_17}
```
## Author:
Navii
---
