## **Challenge Name: The Symphony of Greatness**

### **Solves**
- **Solves**: 40
- **Points**: 200

### **Approach**

Hey everyone, myself 'modernlouis'. I remember starting to explore music outside of my native language years ago. Back then, I was just a kid, trying something completely new and unfamiliar. At first, I did it to feel included with others who were effortlessly singing along to the most popular songs of the time.

Over the years, I listened to a lot of artists, but for a long time, I couldn’t settle on an all-time favorite. That changed during the recent pandemic. With all the extra time on my hands, I dove deeper into my love for music. Slowly and without even realizing it, I found myself drawn to a specific kind of sound.

What kind of music, you ask?
Well, not the ones filled with meaningless words just to make rhymes. Not the albums entirely focused on heartbreak stories. And definitely not the tracks made just to curse or diss someone—come on, let’s move past that.

I admire musicians who showcase raw vocal talent, seamlessly blend different genres, and have a a signature sound that was instantly recognizable and highly danceable.

Now, here’s the challenge:
Your task is to figure out which band I’m talking about. The biggest hint?
Me...

Flag Format:
The Flag is the band's name followed by their most streamed song, in this format:
ACECTF{band_name_song_name}

Example:
If the band is One Direction and their most streamed song is Night Changes, then the flag would be:
ACECTF{0n3_d1r3c710n_n16h7_ch4n635}

---

### **Approach**

## **Approach**

We start with **Sherlock** and find two leads: **YouTube** and **Genius**. For the sake of this write-up, I'll walk you through the intended step by step:

### **1. YouTube Investigation**

The first lead is a YouTube profile:

[**YouTube:**](https://www.youtube.com/@modernlouis)

Visiting the profile section, we find some interesting information:

![YT](Resources/image1.png)

A **Makromusic** account is linked: [https://makromusic.com/u/modernlouis](https://makromusic.com/u/modernlouis). Let's check it out.

![Makromusic](Resources/image2.png)

The bio states:
> *Ok, I guess we're all "Genius". So if you haven't solved yet, here's the hint - "Maybe they're technically not a band after all".*

Now, we know this group **is not a band**. We also have an additional hint: **“Genius”**, which leads us to the next profile.

---

### **2. Genius Profile Investigation**

On **Genius**, the bio contains some very interesting information:

![Genius](Resources/image3.png)

The bio also provides a cryptic string:

> *Also, let’s see if you can make some sense out of this random string I found from some music streaming platform:*
> `313vqcsij2k5ukfgqwhu27sr4l64`

We need to figure out where this username is used. One way is to check major music streaming platforms such as **Amazon Music** and **Spotify**, which have the following URL patterns:

- Amazon Music Profile : https://music.amazon.in/profiles/some_string
- Spotify Profile : https://open.spotify.com/user/some_string

Alternatively, we can trust **Sherlock** to track down the username.

```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ sherlock 313vqcsij2k5ukfgqwhu27sr4l64
/home/kali/.local/lib/python3.12/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.20) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
[*] Checking username 313vqcsij2k5ukfgqwhu27sr4l64 on:

[+] AllMyLinks: https://allmylinks.com/313vqcsij2k5ukfgqwhu27sr4l64
[+] BiggerPockets: https://www.biggerpockets.com/users/313vqcsij2k5ukfgqwhu27sr4l64
[+] Spotify: https://open.spotify.com/user/313vqcsij2k5ukfgqwhu27sr4l64
[+] mastodon.cloud: https://mastodon.cloud/@313vqcsij2k5ukfgqwhu27sr4l64

[*] Search completed with 4 results
```

Sherlock doesn't disappoint—we find the **Spotify** account!

---

### **3. Spotify Investigation**

Visiting the **Spotify** profile, we find the following playlists:

![Spotify](Resources/image4.png)

Opening the **first playlist**, we find the intended **band name: "Modern Talking"**.

To confirm their **most streamed song**, we check Spotify’s rankings, which reveal:

**Most Streamed Song:** *Cheri Cheri Lady*

---

### **Final Flag Submission**

Transforming the information into the required flag format:

```
ACECTF{m0d3rn_74lk1n6_ch3r1_ch3r1_l4dy}
```

---

### **Flag**
```
ACECTF{m0d3rn_74lk1n6_ch3r1_ch3r1_l4dy}
```
---
