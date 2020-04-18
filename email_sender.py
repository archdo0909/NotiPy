import sys
import smtplib
import pickle
from email.mime.text import MIMEText

class MessageSender:
    def __init__(self,
                 api_key=None,
                 api_secret=None,
                 username=None,
                 password=None,
                 send_addr=None,
                 recv_addr=None):

        self.api_key = api_key
        self.api_secret = api_secret
        self.username = username
        self.password = password
        self.send_addr = send_addr
        self.recv_addr = recv_addr

    def send_email(self, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.send_addr, self.recv_addr, message.as_string())
        server.quit()
        print("Mail has been sent")

if __name__ == '__main__':
    sender = MessageSender( username='',
                            password= ''
                            send_addr='',
                            recv_addr='')
                        
    msg = MIMEText("TEST")
    sender.send_email(msg)
        
