from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_receive():
	"""Respond to incoming calls with a simple text message."""
	# Start our TwiML response
	resp = MessagingResponse()

	message = request.values.get("Body", None)
	print(message)

	if "STOP" in message.upper():

	if "SKIP" in message.upper():

	if "BIEBER" in message.upper():
		# rickroll pls


# stop, skip etc

	resp.message("YOU HAVE BEEN HEARD!")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)