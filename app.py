from flask import Flask, request ,render_template
from twilio.twiml.messaging_response import MessagingResponse 

from twilio.rest import Client 





app = Flask(__name__)

@app.route("/" , methods = ['GET' , 'POST'])

def index():
    
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        pname = request.form['pname']


        sid = 'AC454a7be24d70a5d270685218fafb0ec8'
        auth = 'b45517e9408a9795b47a1b41b0d55f8c'

        client = Client(sid,auth)

        message = client.messages.create(
             from_='whatsapp:+14155238886',  
             body='hello ' +  str(fname) + " " +  str(lname) +  ' welcome to Tanzible',   
             to='whatsapp:+91'+str(pname)
        )

        return 'registration successfully'

        

        
    
    return render_template('index.html')

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message

    # Create reply
    resp = MessagingResponse()
    resp.message("Thank you for contacting us! Our team will shortly in touch with you ")

    return str(resp)


if __name__ == "__main__": 
    app.run(debug=True)