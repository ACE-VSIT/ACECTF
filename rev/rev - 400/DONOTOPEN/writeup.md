# **Challenge Name: DONOTOPEN**

## **Solves**
- **Solves**: -
- **Points**: 400

## **Description**
A suspicious script file seems to be hiding something important, but it refuses to cooperate. It's obfuscated, tampered with, and demands a password. Unravel the mystery to uncover the hidden flag.

## **Approach**

### 1. File Type Analysis
The challenge begins with identifying the file type. Running `file script.sh` revealed that it’s a shell script, but it wouldn’t execute properly due to an error:  


### 2. Hex Editor Investigation
To investigate further, the script was opened in a hex editor. It was apparent that the MD5 checksum embedded in the script had been corrupted and replaced with random hex values.


- After correcting the checksum to match the expected value, the script was able to execute.

### 3. Password Prompt
Upon execution, the script demanded a password. However, the script was obfuscated, making it challenging to locate where the password was being checked.


### 4. Analyzing the Script Behavior
Running the script triggered a visit to the **acevips website**, which hinted at being a clue. However, after thoroughly inspecting the site, no useful information was found.

### 5. Temporary File Discovery
By carefully analyzing the obfuscated shell script, it was observed that it extracted a **temporary Python file** in the `/tmp` directory, executed it, and then cleaned it up after execution to leave no trace.

- Using Kali Linux, I was able to pause the execution and locate the extracted temporary file.

### 6. Inspecting the Python File
The Python file contained **thousands of fake flags** designed to mislead solvers. These fake flags were stored in a massive list to confuse anyone inspecting the file.

- By scrolling to the very end of the file, I discovered the **real password** and the **flag**.

### 7. Submitting the Password
Using the password found at the end of the Python file, I entered it into the script. This revealed the flag.
password - ACE@SE7EN

## **Flag**

ACE{e2e3619b630b3be9de762910fd58dba7}
