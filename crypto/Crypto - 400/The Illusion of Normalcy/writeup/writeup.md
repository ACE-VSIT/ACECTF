# **Challenge Title: The Illusion of Normalcy**

### **Solves**
- **Solves**: 0
- **Points**: 400

## **Description**
Elliot Alderson has discovered encrypted notes and hashes across various devices, each holding pieces of his past and secrets about the  Army. Your mission is to crack these hashes, uncover the hidden messages, and dismantle the Dark Army's plans.

Flag Format - ACECTF{Level-1-Flag + Level-2-Flag + Level-3-Flag}

## **Challenge Levels**

### **Level I: The Illusion of Normalcy**

#### **Scenario**
Elliot has found an encrypted note on his computer, seemingly simple but hiding a deeper meaning. The hash is encrypted using **MD5**, and the password resonates with themes of his journey.

#### **Hash**
8e45fba5043614adf931a800cb95b45d


#### **Solution**
Players can crack the hash using:
- A wordlist (e.g., those found in Kali Linux)  
- A brute-force MD5 cracker.

**Correct Password:** `eliot@cute`

---

### **Level II: The Truth About Mr. Robot**

#### **Scenario**
Elliot uncovers a new hash on his father's old computer, tied to clues about Edward Alderson’s identity. While investigating, he finds old passwords that hint at familial details:

#### **Old Passwords Found**
- `MagdaAlderson123`  
- `Eliot33Alderson1986`  
- `Darlene890Alderson`

#### **Hash**
8388c15caa3de12a162212f786a5d27e13d4bee342080282b66be8e02beca979

*(SHA256)*

#### **Solution**
**Correct Password:** `Alderson43Eliot1995`  
- It references Edward's death date instead of his birthdate, making it harder to guess.

#### **Hints**
- Use tools like **Hashcat** or create a custom dictionary based on:
  - Edward Alderson's DOB, age, name, and last name.
- Filtering the dictionary with common variations can help refine guesses.

---

### **Level III: The Collapse of Dark Army**

#### **Scenario**
Elliot reaches the heart of the Dark Army's operations. A final encrypted file holds several hashes used by key members. Cracking these is the only way to stop Whiterose and dismantle her plans.

#### **Hash**
SHA512: 51c648c79b59b6f7122bfa1f08f0bbf3282a7e8bce4e394c1da58bb3f57df8f3be0208b0b0ce3cc56f83028b8ba61c1b3f7fae17ffaf44d175f202f0bb1120e6


#### **Solution**
**Correct Password:** `WhiteRoseLovesTime`  
- This reflects a deep reference to Whiterose's obsession with time, a recurring theme in the show.

#### **Hints**
- A note in the file mentions Whiterose's story and hints at **"Township Power Plant"** or **"Time."**
- Players can deduce that **"time"** plays a significant role in her narrative and is key to solving this level.

---

## **General Guidance for All Levels**

### **Tools**
- **John the Ripper**
- **Hashcat**
- Online hash crackers
- **Kali Linux dictionaries** or custom wordlists for cracking hashes.

### **Strategies**
- Focus on the show's themes for passwords, such as:
  - Familial ties
  - Emotions
  - Philosophical ideas.
- Pay attention to in-game clues and references to the series, as they often provide direct hints about the passwords.

---

## **Final Flag**
The complete flag will be the combination of all the flags found.
ACECTF{eliot@cute+Alderson43Eliot1995+WhiteRoseLovesTime}
