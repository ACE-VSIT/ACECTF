## **Challenge Name: Token of Trust**

### **Solves**
- **Solves**: 202
- **Points**: 200

### **Description**
At first, this web app seems straightforward, but there’s something more lurking beneath the surface. It relies on a token for user authentication, but not everything is as secure as it seems. Look closely, and you might discover that the system’s trust can be manipulated.

The secret is hidden within the way this token is used. Can you find the key to unlock what’s been
concealed? The challenge is waiting for you to crack it.

### **Approach**

1. Use **cURL** to send a **POST** request to **/login** for getting the JWT Token [Main Page](Resources/1.png) [/login](Resources/2.png) [cURL Request](Resources/3.png)

```
curl -X POST http://localhost:9999/login -H "Content-Type: application/json" --data"{\"user\":\"ace\",\"pass\":\"ctf\"}"
```

2. Exploring the **/flag** path using the received token [cURL Request](Resources/4.png)

```
curl -X POST http://localhost:9999/flag -H "Content-Type: application/json" --data "{\"token\":\" \"}"
```

3. Decoding the token using **JWT.io** or other similar platforms [Guest Token](Resources/5.png)

4. Manipulating the **user** field in the **payload** of the JWT from **‘guest’** to **‘admin’** [Admin Token](Resources/6.png)

5. Using the **modified token** to send a **POST** request to the **/flag** path [Flag](Resources/7.png)

```
curl -X POST http://localhost:9999/flag -H "Content-Type: application/json" --data"{\"token\":\"modified_token \"}"
```
### **Flag**
```
ACECTF{jw7_cr4ck3d_4dm1n_4cc355_0b741n3d}
```

