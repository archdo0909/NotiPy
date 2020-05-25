import sys
import requests
from pprint import pprint

from note.messenger.messenger import messenger

class Line(messenger):
    def __init__(self):
        super().__init__()
        
    def print_all(self):
        print(self.API_PASSWORD)
        print(self.API_ID)
        print(self._recevier)
        print(self._msg)

    def send_message(self, img):
        TARGET_URL = "https://notify-api.line.me/api/notify"
        headers = {'Authorization': 'Bearer ' + self._recevier}
        payload = {'message': self._message}
        files = {'imageFile': open(img, 'rb')} if img else None
        r = requests.post(TARGET_URL, headers=headers, params=payload, files=files)
        if files:
            files['imageFIle'].close()
            return r.status_code
        print("Message has been sent")
    
        
    
