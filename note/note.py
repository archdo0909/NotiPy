

from note.messenger.email.mail import Mail

class NOTE:

    def __init__(self):
        print('initialize')

    def Email(self, API_ID, API_PASSWORD):
        print("EMAIL Selected")
        return Mail(API_ID, API_PASSWORD)