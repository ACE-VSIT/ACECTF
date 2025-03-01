## **Challenge Name: Fractured Frames**

### **Solves**
- **Solves**: 43
- **Points**: 300

### **Description**
A forensic investigator retrieved this image from a suspect’s device, but something isn’t right. The structure shows unusual modifications. Could it be that vital information was concealed rather than erased?

Flag Format: ACECTF{3x4mpl3_fl4g}

---
### **Approach**

1. **Inspect the File**

The first step in any forensics challenge is to gather basic information about the file. We start by running the `file` command:

```sh
file hidden_image.jpg
```

It confirms that the file is a JPEG image.

2. **Analyze the Hex Structure**

Since the flag was written at the bottom of the image, we suspect that modifications in the image header might have caused part of the image to be hidden. We use `xxd` to view the hex data:

```sh
xxd hidden_image.jpg | less
```

We locate the **Start of Frame (SOF0) marker**, which usually looks like this:

```
FF C0 00 11 08 01 15 00 B6 03 01
```

However, in this file, it has been altered to:

```
FF C0 00 11 08 00 FF 00 B6 03 01
```

This modification has changed the **height** of the image, making the bottom part—including the flag—disappear from view.

---

3. **Restore the Original Dimensions**

To restore the hidden portion of the image, we correct the SOF0 marker using `hexedit`:

```sh
hexedit hidden_image.jpg
```

1. Search for `FF C0 00 11 08 00 FF 00 B6 03 01`.
2. Modify the bytes `08 00 FF` to `08 01 15`, restoring the original height.
3. Save the changes and exit.

---

4. **Extract the Flag**

Now that the correct height is restored, we open the image using any standard viewer. The previously hidden portion becomes visible, revealing the flag at the bottom of the image.

---

### **Flag**

```
ACECTF{th1s_sh0uld_b3_en0u6h}
```

## Author

Navii

---