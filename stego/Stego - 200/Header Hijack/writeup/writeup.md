## **Challenge Name: Corrupt Vision**

### **Solves**
- **Solves**: - 68
- **Points**: 100  

### **Description**
A secret agent's intercepted video file refuses to play. A mysterious checksum file was found alongside it. Your task is to repair the file and retrieve the flag.
---

### **Attachments**

- [HeaderHijack.zip](../challenge-files/HeaderHijack.zip)

---

### **Approach**

1. **Extract the Files**
    - Unzip the provided ZIP file using the `unzip` command:
      ```bash
      unzip <filename>.zip
      ```
    - The ZIP file contains:
      - `checksum` (contains the checksum for verification)
      - `<filename>.mp4` (a non-functional video file)

2. **Analyze the Non-Functional MP4 File**
    - Attempt to play the MP4 file.
    - If the file fails to play, its MP4 header might be corrupted.
    - Extract the Hexdump using a hex editor:
      - **Windows:** Bliss, HxD
      - **Linux:** Hexcurse, `xxd`
    - Open the MP4 file in the hex editor to analyze its structure.

3. **Inspect the Header Section**
    - Look for clues in the header.
    - The header will contain a message like **“look down closely”**.
    - Scroll a few lines down to find a **fake flag** (e.g., `FLAG{fake_flag_here}`).
    - The fake flag is meant to mislead; ignore it.

4. **Correct the MP4 Header**
    - Identify the correct MP4 header format:
      - Compare the corrupted header with a standard MP4 header.
      - Use reference material or MP4 file structure documentation.
    - Modify the header:
      - Edit the file in the hex editor to replace the corrupted header with the correct MP4 header values.
    - Save the changes as a new MP4 file:
      ```bash
      mv <corrupted_file>.mp4 fixed_filename.mp4
      ```

5. **Verify the Integrity**
    - Use the checksum file to verify the repaired file:
      ```bash
      sha256sum fixed_filename.mp4
      ```
    - Compare the output checksum with the value in the checksum file.
    - If the checksum matches, the file has been repaired correctly.

6. **Play the Fixed Video**
    - Open the repaired MP4 file in a media player (VLC, Windows Media Player, etc.).
    - Watch the video to retrieve the **real flag**

---

### **Key Tools Required**
- **Hex editors:** Bliss, HxD (Windows) / `xxd`, Hexcurse (Linux)
- **Media player:** VLC or equivalent
- **File integrity tools:** `sha256sum` or similar

---

### **Flag**
```
ACECTF{d3c0d3_h3x_1s_fun}
```