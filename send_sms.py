import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='bd725b35fa0e8865246120da323bbd20522a53ef87cac32fb59c37dc1b295ee9'
)

sms = africastalking.SMS

class send_sms():
        
        #TODO: Send message
        def sending(self):
            # Set the numbers in international format
            recipients = ["+254722123123"]
            # Set your message
            message = "Hey AT Ninja!";
            # Set your shortCode or senderId
            sender = "44314"
            try:
                response = sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')

        pass #delete this code