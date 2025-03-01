## **Challenge Name: jumPIEng**

### **Solves**
- **Solves**: 217
- **Points**: 200

### **Description**

Harry, a rookie in CTFs just begun learning binary exploitation and was fascinated with how PIE works. So, he now believe that no 
matter how much information you have about the addresses, you cannot leak the flag from his binary because it has PIE enabled. 
Good luck proving him wrong.

Connect using nc 34.131.133.224 12346

---

### **Approach**  

Download the given binary and run checksec,

```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ checksec ./redirection       
[*] '/home/kali/Desktop/tmp/redirection'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No
```

Canaery found along with PIE.

A PIE and Canary enables executable binary. When run, gives the main address function address and then asks for address to jump to. We need to
enter the address of the redirect_to_success function to get the flag.txt printed out. But, since it's a PIE enabled, we need to calculate the 
offset of the function from main using local copy first and then add that offset value from the provided netcat connection's main function and send
it back within 3 seconds, so scripting is required.

Source code - 

```c
#include <stdio.h>
#include <stdlib.h>

// Declare function prototypes
void redirect_to_success();
void redirect_to_abyss();
void leak_address();

int main() {
    unsigned long target_address;
    leak_address();
    printf("Enter a redirection address (e.g., 0x12345): ");
    if (scanf("%lx", &target_address) != 1) {
        fprintf(stderr, "Invalid input. Unable to redirect.\n");
        return 1;
    }
    printf("Redirecting to address 0x%lx!\n", target_address);
    void (*redirect_function)() = (void (*)())target_address;
    redirect_function();

    return 0;
}

void redirect_to_success() {
    // Read flag
    FILE *flag_file = fopen("flag.txt", "r");
    if (flag_file == NULL) {
        printf("Redirection failed.\n");
        return;
    }
    char flag[64];
    if (fgets(flag, sizeof(flag), flag_file)) {
        printf("Flag: %s\n", flag);
    }
    fclose(flag_file);
}

void redirect_to_abyss() {
    printf("You have been redirected to the abyss!\n");
}

void leak_address() {
    printf("Hint: The main function is located at %p\n", (void *)main);
}
```

Solve script [script.py](Resources/script.py)


---

### **Flag**
```
ACECTF{57up1d_57up1d_h4rry}
```
---
