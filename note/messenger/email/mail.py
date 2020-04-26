import sys
import smtplib
from email.mime.text import MIMEText
from pprint import pprint

from note.messenger.messenger import messenger

class Mail(messenger):
    def __init__(self, API_ID, API_PASSWORD):
        super().__init__(API_ID, API_PASSWORD)
        self._email_msg = {}
        
    def print_all(self):
        print(self.API_PASSWORD)
        print(self.API_ID)
        print(self._recevier)
        print(self._msg)

    def send_email(self):
        try:
            message = MIMEText(self._msg)
        except:
            print("Please write your message")

        #message = self._email_msg.copy()
        message['From'] = self._email_msg['From']
        message['To'] = self._email_msg['To']
        message['Subject'] = self._email_msg['subject']

        ################DISPLAY################
        pprint(f'From : {message["From"]}')
        pprint(f'To : {message["To"]}')
        pprint(f'Subject : {message["subject"]}')
        pprint('Contents : ')
        print('\n')
        pprint(self._msg)
        #######################################
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.API_ID, self.API_PASSWORD)
        server.sendmail(self.API_ID, self._recevier, message.as_string())
        server.quit()
        print("Mail has been sent")
    
    @property
    def set_subject(self):
        return self._email_msg['subject']

    @set_subject.setter
    def set_subject(self, subject):
        self._email_msg['subject'] = subject

    @property
    def set_from(self):
        return self._email_msg['From']

    @set_from.setter
    def set_from(self, ME):
        self._email_msg['From'] = ME

    @property
    def set_to(self):
        return self._email_msg['To']

    @set_to.setter
    def set_to(self, you):
        self._email_msg['To'] = you

    
        
    