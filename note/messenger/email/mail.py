import sys
import smtplib
from email.mime.text import MIMEText

from note.messenger.messenger import messenger

class Mail(messenger):
    def __init__(self, API_ID, API_PASSWORD):
        super().__init__(API_ID, API_PASSWORD)
        
    def print_all(self):
        print(self.API_PASSWORD)
        print(self.API_ID)
        print(self._recevier)
        print(self._msg)

    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.API_ID, self.API_PASSWORD)
        server.sendmail(self.API_ID, self._recevier, self._msg.as_string())
        server.quit()
        print("Mail has been sent")
    
    @property
    def set_subject(self):
        return self._msg['subject']

    @set_subject.setter
    def set_subject(self, subject):
        self._msg['subject'] = subject

    @property
    def set_from(self):
        return self._msg['From']

    @set_from.setter
    def set_from(self, ME):
        self._msg['From'] = ME

    @property
    def set_to(self):
        return self._msg['To']

    @set_to.setter
    def set_to(self, you):
        self._msg['To'] = you

    
        
    