const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000; 
const flag = process.env.FLAG || "flag{fake_flag}";

function replaceFlagInErrorLog(callback) {
  const filePath = '/var/log/apache2/error.log';
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return callback(err, null);
    }

    // Perform the replacement
    const modifiedData = data.replace('{{FLAG}}', flag);
    callback(null, modifiedData);
  });
}

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Main Area
app.get('/content', (req, res) => {
  let language = req.query.lang || 'en';
  let filePath = path.join(__dirname, 'languages', `${language}`);

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading file');
    }

    if (filePath.includes("/log/apache2/error.log")) {
      replaceFlagInErrorLog((err, modifiedData) => {
        if (err) {
          console.error(err);
          return res.status(500).send('Error replacing flag in error log');
        }
        res.send(modifiedData);
      });
    } else {
      res.send(data);
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
