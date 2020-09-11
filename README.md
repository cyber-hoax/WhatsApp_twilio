# WhatApp  twilio integration in python

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

send and receive messages from WhatsApp using twilio and flask 

first for most integrate your number with twilio sandbox
  
 prerequisite:
 ```sh
$ pip install flask
$ pip install twilio
install ngrok
```

### app.py

packagae to  import :

```
from flask import Flask, request ,render_template
from twilio.twiml.messaging_response import MessagingResponse 

from twilio.rest import Client 

```

For sending message  
### app.py

```
@app.route("/" , methods = ['GET' , 'POST'])

def index():
    
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        pname = request.form['pname']


        sid = 'account_sid'
        auth = 'auth_token'

        client = Client(sid,auth)

        message = client.messages.create(
             from_='whatsapp:+14155238886',  
             body='hello ' +  str(fname) + " " +  str(lname) +  ' welcome to Tanzible',   
             to='whatsapp:+91'+str(pname)
        )

        return 'registration successfully'

    return render_template('index.html')
```


### for receiving message 

first we have to configure ngrok to put localhost to on public address

so download ngrok and install it via command line where is you ngrok file
```
./ngrok http 5000 
```
5000 is by default port given by flask 

```
def msg(request):
    if request.method == 'POST':
        resp = MessagingResponse()
        resp.message("Thank you for contacting us! Our team will shortly in touch with you ")
        print(resp)
        return str(resp)
        

```


Thats all folk ! 
