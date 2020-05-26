import sys
import requests

from pprint import pprint

from note.messenger.messenger import messenger

class Telegram(messenger):
    def __init__(self, API_ID, API_PASSWORD):
        super().__init__(API_ID, API_PASSWORD)

    def print_all(self):
        pprint(self.API_ID)
        pprint(self.API_PASSWORD)
        pprint(self._msg)

    def send_message(self):
        BASE_URL = "https://api.telegram.org/bot"
        SEND_URL = "/sendMessage?chat_id="
        TEXT_URL = "&parse_mode=Markdown&text="

        send_message = \
                    BASE_URL + self.API_PASSWORD + \
                    SEND_URL + self.API_ID + \
                    TEXT_URL + self._msg

        requests.get(send_message)

        print("Message has been sent!")




    