const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from loginScreen folder
app.use(express.static(path.join(__dirname, "frontend/src/screens/loginScreen")));

// Redirect root to login.html
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "frontend/src/screens/loginScreen/login.html"));
});

// Serve login page
app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "frontend/src/screens/loginScreen/login.html"));
});

// Serve signup page
app.get("/signup", (req, res) => {
  res.sendFile(path.join(__dirname, "frontend/src/screens/loginScreen/signup.html"));
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

