'use strict';

const fs = require('fs')
const http = require('http')
const https = require('https')
const express = require('express')
const nodeRequest = require('request')
const bodyParser = require('body-parser')

var port = process.env.PORT

var signals = {}
signals["Power TV"] = [9010, 4474, 584, 544, 584, 544, 584, 544, 584, 542, 584, 544, 584, 544, 556, 570, 584, 544, 582, 1672, 584, 1670, 584, 1672, 584, 1670, 584, 1670, 584, 1672, 582, 1672, 582, 544, 584, 1672, 584, 542, 558, 1698, 584, 544, 582, 1672, 584, 542, 584, 544, 584, 544, 582, 544, 584, 1670, 558, 570, 584, 1670, 582, 544, 582, 1672, 584, 1670, 584, 1670, 582]
signals["Source"] = [9004, 4500, 560, 568, 560, 568, 558, 568, 560, 568, 560, 568, 558, 568, 558, 568, 560, 566, 560, 1694, 560, 1696, 558, 1696, 560, 1694, 560, 1694, 560, 1696, 560, 1694, 560, 568, 560, 568, 560, 1694, 560, 568, 560, 568, 558, 1694, 560, 568, 560, 568, 558, 568, 560, 1694, 560, 568, 560, 1694, 560, 1696, 558, 568, 560, 1694, 560, 1696, 560, 1694, 560]
signals["DTV"] = [9150, 4352, 682, 446, 706, 422, 678, 448, 680, 448, 678, 448, 696, 430, 682, 444, 680, 446, 706, 1548, 706, 1546, 682, 1574, 678, 1576, 678, 1576, 678, 1578, 680, 1574, 680, 446, 678, 1576, 678, 1576, 680, 446, 678, 1576, 706, 422, 706, 422, 680, 446, 678, 448, 704, 422, 678, 448, 678, 1576, 706, 420, 676, 1578, 678, 1578, 680, 1574, 680, 1574, 678]
signals["Down"] = [9134, 4350, 678, 448, 682, 446, 704, 422, 680, 446, 708, 420, 682, 446, 680, 446, 680, 448, 682, 1574, 682, 1574, 678, 1574, 682, 1574, 680, 1576, 682, 1572, 704, 1550, 680, 448, 680, 1574, 682, 444, 678, 1576, 680, 1574, 682, 444, 678, 448, 682, 446, 682, 446, 706, 422, 706, 1546, 680, 448, 708, 418, 680, 1574, 680, 1574, 706, 1548, 682, 1572, 708]
signals["Enter"] = [9152, 4350, 680, 446, 682, 446, 676, 450, 680, 448, 678, 448, 708, 420, 682, 446, 682, 444, 676, 1578, 680, 1574, 684, 1570, 682, 1574, 682, 1572, 708, 1546, 680, 1574, 678, 450, 682, 444, 680, 446, 678, 450, 678, 448, 708, 1546, 678, 448, 682, 446, 706, 418, 682, 1574, 678, 1576, 678, 1576, 680, 1574, 680, 448, 678, 1574, 682, 1572, 680, 1574, 682]

// Certificate
/*const privateKey = fs.readFileSync('/etc/letsencrypt/live/coloc.servebeer.com/privkey.pem', 'utf8');
const certificate = fs.readFileSync('/etc/letsencrypt/live/coloc.servebeer.com/cert.pem', 'utf8');
const ca = fs.readFileSync('/etc/letsencrypt/live/coloc.servebeer.com/chain.pem', 'utf8');

const credentials = {
	key: privateKey,
	cert: certificate,
	ca: ca
};*/

var app = express()

/*app.post('/api/scene/kodi', function(req, res) {
    var timings = ""
    for (var i = 0; i < signals["Source"].length; i++) {
        timings += signals["Source"][i]
        if (i != (signals["Source"].length - 1)) {
            timings += ", "
        }
    }
    nodeRequest.post("http://192.168.1.56/play", {form: {'timings': timings}})

    res.send(JSON.stringify({"fulfillmentText": "Changement de la source pour kodi"}))
})*/

app.get('/', function(req, res) {
    //res.send(JSON.stringify({Hello: "World"}));
    var timings = ""
    for (var i = 0; i < signals["Source"].length; i++) {
        timings += signals["Source"][i]
        if (i != (signals["Source"].length - 1)) {
            timings += ", "
        }
    }
    nodeRequest.post("http://192.168.1.56/play", {form: {'timings': timings}})

    res.send(JSON.stringify({"fulfillmentText": "Changement de la source pour kodi"}))
})

app.listen(port, () => {
    console.log("Server is up ...");
})