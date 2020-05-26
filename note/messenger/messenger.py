class messenger:
    def __init__(self, API_ID, API_PASSWORD):
        self.API_ID = API_ID
        self.API_PASSWORD = API_PASSWORD
        self._msg = ""

    @property
    def recevier(self):
        return self._recevier

    @property
    def message(self):
        return self._msg

    @recevier.setter
    def recevier(self, recv_addr):
        self._recevier = recv_addr
    
    @message.setter
    def message(self, text):
        self._msg = text