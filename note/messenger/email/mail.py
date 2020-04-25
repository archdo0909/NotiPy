from note.messenger.messenger import messenger

class Mail(messenger):
    def __init__(self, API_ID, API_PASSWORD):
        super().__init__(API_ID, API_PASSWORD)
        
    def print_all(self):
        print(self.API_PASSWORD)
        print(self.API_ID)
        print(self._recevier)
        print(self._msg)
    