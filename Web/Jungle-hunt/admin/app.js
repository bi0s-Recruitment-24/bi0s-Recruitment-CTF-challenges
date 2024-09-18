// Dependencies
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const cookieParser = require('cookie-parser');
const path = require("path")
const expressSession = require('express-session');
const ejs = require('ejs');
const { SHA256 } = require("crypto-js");

// Const Variables
const PORT = process.env.PORT || 1337;
const FLAG = process.env.FLAG || "bi0s{jungl3_3sc4p3_15_n0t_345y}";
const questions = JSON.parse(fs.readFileSync('questions.json', 'utf8')).questions;

// Creating an express app
const app = express();
app.disable('x-powered-by');

// Setting the static directory
app.use(express.static(__dirname + '/public'));

// Using template engine
app.set('view engine', 'ejs');

// Using cookieParser, bodyParser middleware
app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: true }));

// Creating secret
const plainSecret = "We_Are_Inevitable";
const secret = SHA256(plainSecret).toString();

// Defining the session.
app.use(expressSession({
    secret: secret,
    saveUninitialized: true,
    resave: true
}));

// Solved?
let solved = 0;
let status = "";

// Routes
app.get('/', (req, res) => {
  res.cookie('Answer-7', 'Eat until you are full!')

  let statusToRender = "";

  switch (status) {
      case 'Wrong!':
          statusToRender = status;
          status = "";
          break;
      case 'Correct!':
          statusToRender = status;
          status = "";
          break;
      case 'Flag':
          statusToRender = "Your gift: " + FLAG;
          status = "";
          break;
      default:
          break;
  }

  res.render('main', {
      question: questions[solved].question,
      status: statusToRender
  });
});

app.get('/robots.txt', (req, res) => {
    res.sendFile(__dirname + "/robots.txt");
});

app.get('/secret', (req, res) => {
    res.render("answer", {
      answer: 'Answer-5 : Dangerous, Web Crawler'
    });
});

app.get('/headers', (req, res) => {
    res.setHeader("Answer-2", "SHH! Some one found us");
    res.render("answer", {
      answer: "There is something here..."
    });
});

app.get('/welcome', (req, res) => {
    res.render("answer", {
      answer: "Answer-1: I am new here!"
    });
});

app.post('/submitAnswer', (req, res) => {
    let answer = req.body.answer.trim();
    console.log("Answer Recieved:", answer);
    console.log("Answer:", questions[solved]['answer']);
    console.log("Current Question:", solved);
    if (answer === questions[solved]['answer']) {
        if (solved === 8) {
          status = "Flag"
          res.redirect('/')
        } else {
          solved++;
          status = "Correct!";
          res.redirect('/')
        }
    } else {
        status = "Wrong!";
        res.redirect('/');
    }
});

app.get('/escape', (req, res) => {
  if (solved === 8) {
    res.render("answer", {answer: "Answer-8: Let's escape!"})
  } else {
    res.render("404");
  }
});

app.get('*', (req, res) => {
    res.render('404');
});

// Listening on Port ${PORT}
app.listen(PORT, () => console.log(`Server is running on ${PORT}`));
