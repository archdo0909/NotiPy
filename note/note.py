from note.messenger.email.mail import Mail
from note.messenger.line.line import Line

class NOTE:

    def __init__(self):
        print('initialize')

    def Email(self, API_ID, API_PASSWORD):
        print("EMAIL Selected")
        return Mail(API_ID, API_PASSWORD)

    def Line(self, API_ID, API_PASSWORD):
        print("Send Message through LINE")
        return Line(API_ID, API_PASSWORD)
