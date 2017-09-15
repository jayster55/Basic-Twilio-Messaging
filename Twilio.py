from twilio.rest import Client

#Your account sid and auth token from twilio.com/user/account
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="Here is a message",
                                     to="+14159352345", #your phone number
                                     from_="+14158151829") #twilio phone number
print message.sid
