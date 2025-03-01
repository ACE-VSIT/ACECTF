## **Challenge Name: Buried Deep**

### **Solves**
- **Solves**: 226
- **Points**: 100  

### **Description**
"I’m not a hacker. I’m just someone who wants to make the world a little better. But the world isn’t
going to change itself."

**The flag content should be in lowercase letters only.**

### **Approach**

1. Opening the **robots.txt** file after decoding the quote reference from Mr. Robot TV Series [Robots.txt File](Resources/1.png)

2. Traversing the **disallowed paths** mentioned in the **robots.txt** file

3. Finding the **first part** of the flag in the **/buried** route
It is in **ASCII** format [ASCII](Resources/2.png) [ASCII Decoded](Resources/3.png)

4. Finding the **second part** of the flag in the **/secret_path** route. 
It is in **Morse Code** format [Morse Code](Resources/4.png) [Morse Code Decoded](Resources/5.png)

5. The **/encrypted** route hints towards the **remaining part** of the flag being in the **CSS file**
After **inspecting the page source**, the **third part** of the flag is found in the **flag** section of the **CSS file**.
It is in **ROT47** format [ROT 47](Resources/6.png) [ROT 47 Decoded](Resources/7.png)

### **Flag**
```
ACECTF{1nf1l7r471ng_7h3_5y573m_15_345y_wh3n_y0u_kn0w_wh3r3_7h3_53cr3t5_4r3_bur13d}
```

