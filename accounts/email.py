from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

class user_mail:

    def __init__(self,  recipients):
        self.email_from=settings.EMAIL_HOST_USER
        self.recipients=recipients.split(',')

    def welcome_email(self, name):
        subject = 'Welcome to file coffer'
        message = 'Hi '+name +',<div><br></div><div>Thanks for signingup with Digy-Coffer, a place to store your important digital documents. <br> In digy-coffer we strive to create a safe space on internet to store our personal data so that it can be easily accessible and safe. <br> please feel free to mail back, if you need any assistance.</div><div><br></div><div><br></div><div>with regards,</div><div>Prabu.M</div>'
        msg = EmailMessage(subject, message,self.email_from, self.recipients)
        msg.content_subtype = "html"  # Main content is now text/html
        return msg.send()
    
    def sendVerification_email(self,name,key):
        subject="please verify you mail ID"
        message ="Hi"+name+"<div><br></div><div>Please verify your email address by clicking the following link, the link will be active only for a day.</div><div><br></div><div><br></div><div>"+key+"</div><div><br></div><div>with regards,</div><div>Prabu.M</div>"
        msg = EmailMessage(subject, message,self.email_from, self.recipients)
        msg.content_subtype = "html"  # Main content is now text/html
        return msg.send()

