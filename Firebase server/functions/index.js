const functions = require('firebase-functions');
const express = require('express');
const app = express()

var comp = {fan : 0,light : 0,door : 0}

app.post('/',(request,response) => {
    const temp = request.body;
    comp = temp
    response.json(comp);
})

app.get('/',(request, response) => {
 response.json(comp);
});


exports.api = functions.https.onRequest(app);
