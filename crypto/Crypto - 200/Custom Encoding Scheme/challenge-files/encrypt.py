def e1(t, b, o):
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if len(b) != 168:
        raise ValueError("Invalid Input")
    c = [b[i:i+4] for i in range(0, len(b), 4)]
    with open(o, "w") as f:
        for x, y in enumerate(t):
            z = f"{ord(y):08b}"
            if x < 42:
                a = z[:6]
                d = z[6:] + c[x]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            else:
                a = z[:6]
                d = z[6:]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            print(r)
            f.write(r + "\n")

t = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"
b = "{REDACTED}" # Should be 128 bits
o = "output.txt"

e1(t, b, o)



