const express = require('express')
const nodeRequest = require('request')
const assistant = require('actions-on-google')

const app = express()

app.get('/', function(req, res) {
    res.send('Hello World !')
})

app.get('/api/scene/kodi', function(req, res) {
    res.send('Changing scene to kodi')
})

app.listen(5000, function() {
    console.log('Example app listening on port 5000')
})