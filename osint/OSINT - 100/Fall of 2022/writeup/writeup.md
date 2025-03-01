## **Challenge Name: Fall of 2022**

### **Solves**
- **Solves**: 173
- **Points**: 100

### **Description**

It was a peaceful time — schools were over, college admissions were delayed, and COVID was slowly on the decline. It seemed like the perfect time to relax and check my phone for her txts.

The funny thing is, I never got any. So I considered it just another gloomy year.

Anyways, here’s the domain for this CTF: [acectf.tech](https://acectf.tech)

What? You already knew this domain? Oh, I guess you’ll have no trouble finding the flag then.

Good Luck!

---

### **Approach**  

1. **Analyze the Challenge Description**  
   - The phrase **"check my phone for her txts"** suggests looking for **TXT records** (DNS-related hint).  
   - The challenge explicitly provides the domain: **acectf.tech**.  

2. **Check TXT Records of the Domain**  
   - TXT records often store verification data, SPF records, or even hidden messages.  
   - Run the following command to retrieve TXT records:

   ```bash
   nslookup -type=TXT acectf.tech
   ```
   **OR**
   ```bash
   dig TXT acectf.tech +short
   ```
   
3. **Retrieve the Flag**  
   - The TXT record contains the flag:  
     ```
     ACECTF{y0u_g07_7h3_73x7}
     ```

---

### **Flag**
```
ACECTF{y0u_g07_7h3_73x7}
```
---
