from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from twilio.rest import Client
app = Flask(__name__)
account_sid = 'avhiovav'
auth_token = '16f546a1v1vv'

@app.route('/bot', methods=['GET','POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'frase' in incoming_msg:
    # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
           data = r.json()
           quote = f'{data["content"]} ({data["author"]})'
           client = Client(account_sid, auth_token)

           message = client.messages.create(
           from_='whatsapp:+143121121366',
           body=quote,to='whatsapp:+553313331')
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        q1 = msg.body(quote)
        print(q1)
        responded = True
    if 'gato' in incoming_msg:
    # return a cat pic

        q2 = msg.media('https://cataas.com/cat')
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_='whatsapp:+143121121366',body='Me parece haber visto un lindo un gatito',media_url=['https://cataas.com/cat'],to='whatsapp:+553313331')
        print(q2)
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)
if __name__ == '__main__':
    app.run(port=4000)
