# nothing very important in this file for mid/advanced devs

from twilio.rest import Client

account_sid = "notRealSid"
auth_token = "notRealToken"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from="...",
    body="mesage..."
)
