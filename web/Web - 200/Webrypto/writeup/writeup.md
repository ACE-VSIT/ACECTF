## **Challenge Name: Webrypto**

### **Solves**
- **Solves**: 263
- **Points**: 200  

### **Description**
I think we can all agree that most of us grew up watching the iconic cartoon Tom & Jerry. Every kid would feel that surge of adrenaline during the thrilling chases and chaotic conflicts between the mischievous mouse and the ever-determined cat. The excitement of those scenes—the heart-pounding moments of escape—sometimes felt almost real.

But then, I heard a little rumor: what if all those chases were fake? What if Tom and Jerry were actually friends all along & fought on purpose just to become famous? That revelation shook me. I had no one to ask about this mind-bending twist, so I decided to take matters into my own hands—I created a web app to settle this question once and for all.

I know the truth now. Do you think you can uncover it too?


URL - http://34.131.133.224/Webrypto/

### **Approach**

Vulnerable PHP Code.

if (md5('ACECTF' . $_GET['tom']) == md5('ACECTF' . $_GET['jerry']))

This can be exploited as when we pass an array, let's say tom[] = 1; and jerry[] = 2;

These are different values, but when converted to string for md5 hash conversion, they both get converted to the word 'Array'.

Hence, md5(ACECTFArray) == md5(ACECTFArray) being rendered true.

https://chal.acectf.tech/Webrypto?tom[]=1&jerry[]=2


### **Flag**
```
ACECTF{70m_4nd_j3rry_4r3_4ll135}
```