var express = require('express');
var app = express();
app.use(express.static("./views"));

app.set("view engine", "ejs");


app.get('/', function(req, res) {
    try{
        var info = 'I spy with my little eye, A browser other than secbrowser?';
        if (req.headers['user-agent'] == 'secbrowser') {
            info = "Secbrowser detected!! People REFER me as 'ghostbyte'";
        }
        if (req.headers['referer'] == 'ghostbyte' && req.headers['user-agent'] == 'secbrowser') {
            info = "Hold up! You're not accessing this from my localhost IP!";
        }
        if (req.headers['x-forwarded-for'] == '127.0.0.1' && req.headers['referer'] == 'ghostbyte' && req.headers['user-agent'] == 'secbrowser') {
            info = "Gr8! Now The breached data can only be seen by POSTman.";
        }
        res.render('main', { info: info });
    }catch{
        res.render('main',{info:"Error Occured"});
    }

});

app.post('/', function(req, res) {
    try {
        let info = '';
        if (req.headers['x-forwarded-for'] === '127.0.0.1' && req.headers['referer'] === 'ghostbyte' && req.headers['user-agent'] === 'secbrowser') {
            info = 'Welcome ghostbyte !... Here is your flag: bi0s{h3ad3rs_s4v3d_m3_:)}';
            res.render('main', { info: info });
        } else {
            res.status(403).send('Nopee ;)');
        }
    } catch (error) {
        console.error('POST request error:', error);
        res.render('main', { info: "An Error Occurred" });
    }
});

app.listen(1234, () => { console.log("done") });
