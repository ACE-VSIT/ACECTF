## **Challenge Name: Broken Secrets**

### **Solves**
- **Solves**: 275
- **Points**: 100 

### **Description**
You’ve found a suspicious file, but it seems broken and cannot be opened normally. Your goal is to uncover its secrets.

Submit your answer in the following format: ACECTF{3x4mpl3_fl4g}

---
### **Approach**

1. **Analyze the File Structure**

**Inspect the file format:**
   - Check the file type.
   - If it shows "Microsoft Word Document" or "ZIP archive," proceed to the next step.

**Extract the contents:**
   - Rename the `.docx` file to `.zip`.
   - Unzip the archive to examine its contents.
   - Check the directory structure, which typically includes folders like `word`, `_rels`, and `[Content_Types].xml`.

---

2. **Locate Hidden Files**

**Inspect the `word/media` folder:**
   - Navigate to the `extracted_docx/word/media/` directory. This folder usually contains embedded images.

**Check for anomalies:**
   - Verify the format of the image files.
   - If the file format does not match its extension (e.g., "data" instead of "PNG"), it may have a corrupted header.

---

3. **Repair the Corrupted Image**

**Open the file in a hex editor:**
   - Use a hex editor (e.g., `HxD`, `hexedit`, or `Bless`) to inspect and repair the header of the file.
   - For a valid PNG file, the header should start with the following bytes:
     ```
     89 50 4E 47 0D 0A 1A 0A
     ```

**Correct the header:**
   - Replace the corrupted header bytes with the correct PNG header.
   - Save the file.

**Verify the repaired file:**

   - Open the file in an image viewer to ensure it is valid and get the flag.

---

### **Flag**
```
ACECTF{h34d3r_15_k3y}
```
---

## Author

Navii

---