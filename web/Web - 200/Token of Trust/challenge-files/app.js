const express = require('express');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');

const app = express();

const flag = "ACECTF{jwt_cr4ck3d_4dm1n_4cce55_0bt41n3d!}";

app.use(express.json());
app.use(cookieParser());

// Updated secret key 
const jwt_secret = "supersecureacectfkey@123";

// Route for robots.txt to mislead participants
app.get('/robots.txt', (req, res) => {
  res.send("Disallow: /flag (But hey, who listens to robots anyway?)");
});

app.post('/robots.txt', (req, res) => {
  res.send("Disallow: /flag (Why are you POSTing here? You rebel!)");
});

// Informative route for login hints
app.get('/login', (req, res) => {
  res.send(`
    <h3>Oops! Wrong approach.</h3>
    <p>You can't just waltz in here without a proper <b>POST</b> request.</p>
    <p>Try sending a JSON payload like this: {"user":"ace","pass":"ctf"}.</p>
    <p>Hint: I only care about your request format, not your credentials. 😉</p>
  `);
});

// Main page
app.get('/', (req, res) => {
  res.send(`
    <h3>Welcome to the main page!</h3>
    <p>To log in, visit <b>/login</b>. But remember, POST requests are my love language. 🧡</p>
    <p>PS: Don't forget to set your headers for JSON, or I'll just ignore you. 🙃</p>
  `);
});

// Route to retrieve the flag, requires a valid token
app.post('/flag', (req, res) => {
  const data = req.body.token;
  if (data) {
    const decoded = jwt.decode(data);
    if (decoded && decoded['user'] === 'admin') {
      res.send(flag);
    } else {
      res.send("Sorry, you're not the admin. No flag for you! 😝");
    }
  } else {
    res.send("No token? No flag! Bring me a token, and we'll talk. 👀");
  }
});

// Login route to generate a token for users
app.post('/login', (req, res) => {
  const data = req.body;
  if (data['user'] && data['pass']) {
    // Note: All users get a "guest" token regardless of credentials
    const token = jwt.sign({ 'user': 'guest' }, jwt_secret, { noTimestamp: true });
    res.json({ "token": token });
  } else {
    res.send("Invalid POST data. Did you forget the magic JSON format?");
  }
});

// Start the server
app.listen(9999, () => console.log('Server started on port 9999'));
