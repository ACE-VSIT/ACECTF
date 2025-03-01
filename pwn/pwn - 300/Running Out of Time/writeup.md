# **Running Out of Time**

## **Challenge Description**  

You have been given a mysterious binary named **Running_Out_Of_Time** that asks for a specific number as input. If you provide the correct number, a hidden message will be revealed. However, you have no prior knowledge of what the correct number is.  

Your goal is to reverse-engineer the binary, understand its logic, and retrieve the hidden flag.  

### **Files Provided**  
- `Running_Out_Of_Time` (compiled executable)  

---

## **Walkthrough**  

### **Step 1: Analyzing the Binary**  

Start by running the provided binary:  

```sh
./Running_Out_Of_Time
```

It prompts you to enter a number. If the number is incorrect, it prints:  

```
Incorrect. Please try again.
```

Now, let's check the file type:  

```sh
file Running_Out_Of_Time
```

It should return something like:  

```
Running_Out_Of_Time: ELF 64-bit LSB executable, x86-64, dynamically linked, not stripped
```

Since the binary is **not stripped**, we can easily reverse-engineer it.  

---

### **Step 2: Disassembling the Binary**  

Using `strings` won't reveal useful text, so let's use `Ghidra`, `Cutter`, or `IDA Free` to analyze it.  

In the decompiled code, we notice the following important details:  

- The program generates a number using `srand(time(0))`.  
- It stores the generated number in a variable and compares it to user input.  
- If the number matches, a hidden function (with an obfuscated name) is executed.  

---

### **Step 3: Predicting the Random Number**  

The vulnerability here is that `srand(time(0));` uses the **current epoch time** to initialize the random number generator. If we know the **exact second** the binary starts running, we can **predict** the generated number.  

To get the current epoch time:  

```sh
date +'%s'
```

We can create a simple **brute-force script** in Python to guess the correct number based on the execution time:  

```python
import time
import os

epoch_time = int(time.time())  # Get current epoch timestamp

for t in range(epoch_time - 10, epoch_time + 10):  # Try a range of possible seeds
    os.system(f'echo {t % 100} | ./Running_Out_Of_Time')
```

If the number is correct, the binary will reveal the flag.  

---

### **Step 4: Understanding the Flag Retrieval Mechanism**  

The hidden function in the binary decrypts a hardcoded value using **XOR encryption**. In the obfuscated code:  

```c
char G8kLwq_92[] = {29, 27, 71, 25, 117, 31, 29, 26, 90, 90, 25, 78}; // Encrypted flag
char Zx7R_tpq = 42; // XOR key
```

Each byte is XOR'd with `42` to produce the flag:  

```python
enc_flag = [29, 27, 71, 25, 117, 31, 29, 26, 90, 90, 25, 78]
key = 42
print(''.join(chr(b ^ key) for b in enc_flag))
```

This will reveal the correct flag:  

```
ACECTF{71m3_570pp3d}
```

---
