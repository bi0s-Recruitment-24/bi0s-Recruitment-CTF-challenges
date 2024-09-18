const express = require('express');
const app = express();
const path = require('path');
const cookieParser = require('cookie-parser');
const port = 9015;

app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

function decodeThreeTimes(encodedString) {
    let decodedString = Buffer.from(encodedString, 'base64').toString();
    decodedString = Buffer.from(decodedString, 'base64').toString();
    return Buffer.from(decodedString, 'base64').toString();
}

app.get('/', (req, res) => {
    res.cookie("Auth", "V2pOV2JHTXpVVXNLCg==");
    
    const decodedCookie = decodeThreeTimes(req.cookies['Auth']);
    console.log(decodedCookie);
    if (decodedCookie === "Admin") {
        console.log("GG");
        res.sendFile(path.join(__dirname, 'Real(1).jpg'));
        res.cookie("Flag","Flag{4DMIN_W45NT_CR4ZY}");
    } else {
        res.sendFile(path.join(__dirname, 'index.html'));
    }
});

app.listen(port, () => {
    console.log("listening on " + `${port}`);
});
