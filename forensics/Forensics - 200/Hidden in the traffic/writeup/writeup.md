## **Challenge Name: Hidden in the Traffic**

### **Solves**
- **Solves**: 83
- **Points**: 200 

### **Description**
A whistleblower tipped us off about a secret communication between two devices. We managed to intercept the network traffic, but the flag is hidden within the data. Your task is to analyze the provided PCAP file, uncover the hidden message, and extract the flag.

Submit your answer in the following format: ACECTF{3x4mpl3_fl4g}

### **Approach**

1. **Open the PCAP File**

Launch Wireshark and open the provided PCAP file.

Observe the overall traffic to identify patterns or anomalies. In this case, look for a fishy IP address or the unusual amount of packets sent to the user using a specific protocol.
   The user sent so many ICMP packets to the IP 8.8.8.8 which is not usual. This is a point of interest and we can start investigating here.

2. **Filter for Relevant Packets**

Apply a filter to isolate packets based on their protocol. For example, the flag is encoded in **ICMP** packets, so use the filter:
   ```
   icmp
   ```

Inspect the filtered packets. Each ICMP packet contains one letter of the flag.

3. **Extract the Data**

Click on each ICMP packet in the filtered view and examine the **payload** (data) section in the packet details.

After a character of the flag is sent, there are 12 garbage packets which contain data of A-L alphabets. This is a repeating pattern. 

Filter out these garbage packets as well.
The data is sent in an ASCII code.

4. **Assemble the Flag**

1. Record the letters from the payload of each ICMP packet in sequence.
2. Combine the letters to form the flag.
---

### **Flag**
```
ACECTF{p1n6_0f_D347h}
```

## Author

Navii

---