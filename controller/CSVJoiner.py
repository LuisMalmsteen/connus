from models.Config import Config


class CSVJoiner:
    def __init__(self):
        self.requester = Config()

    def joinReport(self, json):
        string_token_split = self.requester.load_auth_token()
        print(string_token_split)

