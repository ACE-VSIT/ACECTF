## **Challenge Name: Flag-Fetcher**

### **Solves**
- **Solves**: 206
- **Points**: 200  

### **Description**
Hey guys, I created a flag fetcher using some web stacks & technologies. It was supposed to fetch the flag.webp image file which contains the flag but there was some kind of error in doing that. Can you verify it? Maybe just get the flag I don't really care if you fix it or not.

[This should've worked](http://34.131.133.224/Flag-Fetcher/)

### **Approach**

Open up the URL & you'll see it takes a whole lot of time to load up & then hits the endpoint /flag.webp which should contain an image but it doesn't.

Simply inspect & head over to console and you'll see many failed redirects starting with /a,/c,/e,/c,/t,/f,.... up until /}. This should instantly tell you that it's the flag.

Appending all of these will give us the flag.


### **Flag**
```
ACECTF{r3d1r3ct10n}
```