## **Challenge Name: Bucket List**

### **Solves**
- **Solves**: 256
- **Points**: 300  

### **Description**
You know what's a bucketlist?
In simple terms, it's just a list of wishes people want to achieve before the leavee this world.
I found it to be very limiting & ironic because how can you know when you'll leave the world behind? It's better to enjoy every moment and take on every opportunity you can.
One of my whishes though is to pet a cat, do you mind checking this one out. So cute.

[What a cutie patootie!](https://opening-account-acectf.s3.ap-south-1.amazonaws.com/fun/can_we_get_some_dogs/026.jpeg)

### **Approach**

sudo apt install awscli -y

aws --version

aws configure

AWS Access Key ID: (Your AWS access key) - Found on your account
AWS Secret Access Key: (Your AWS secret key) - Found on your account
Default region name: (e.g., us-east-1, ap-south-1 for India)
Default output format: (json, yaml, text, or table – choose json if unsure)

aws s3 ls - list out the buckets.

URL -> https://opening-account-acectf.s3.ap-south-1.amazonaws.com/fun/can_we_get_some_dogs/026.jpeg

Now that we know it's an s3 bucket and the name is opening-account-acectf, let's enumerate.

aws s3 ls s3://opening-account-acectf/

aws s3 sync s3://opening-account-acectf/ downloads     	# to download all our files

Explore and then you find secret.txt with - QUNFQ1RGezdoM180dzVfMTVfbTE1YzBuZjE2dXIzZH0=

Decode Base64 to get the flag.
### **Flag**
```
ACECTF{7h3_4w5_15_m15c0nf16ur3d}
```