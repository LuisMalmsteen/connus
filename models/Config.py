import json

import requests


class Config:

    def __init__(self, days=None, freq=None):
        self._days = days
        self._freq = freq

    def setConfig(self, days, freq):
        pass

    def get_zoho_token(self):
        str_req = 'https://accounts.zoho.com/apiauthtoken/nb/create?SCOPE=ZohoReports/' \
                  'reportsapi&EMAIL_ID=fernando@connus.mx&PASSWORD=Fernando123'
        return requests.post(str_req).text

    def load_auth_token(self):

        with open("Tokens.json", "r+") as token:

            data = json.load(token)

            if not bool(data):
                print('JSON data is empty. Requesting for new token...')
                splitted_str = self.get_zoho_token().split()
                auth = [i for i in splitted_str if 'AUTH' in i]
                auth = {'zohoTokenProd': auth}
                json.dump(auth, token)
                return auth[0].split('=')[1]

            else:
                print("JSON data loaded... Returning token...")
                return data['zohoTokenProd']
