import json
import requests

from models.Config import Config


class MainProcessController:
    def __init__(self):
        self.requester = Config()

    def getAndWriteAlarmsJSON(self):
        auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1YTg0ODMwMjQ3ZjBhZ' \
                     'TEwZTkwMDNkZDciLCJhY2MiOjQsImNtcCI6IjVhMDA3Yzk2YjhhNWU4NDM1ZmQ5MGVhY' \
                     'SIsImlhdCI6MTUzMDY1MDAyNH0.r4qLHckl_Lw7HG3ZHipqm05hOVwLDeZLVjkZUi0mjzI'

        headers = {'Authorization': 'Bearer ' + auth_token, 'content-type': "application/json"}

        alarms = requests.get('http://localhost:8080/v1/reports/alarmsByJson', headers=headers).json()

        with open("alarms.json", "r+") as file:
            json.dump({"alarms":alarms}, file, ensure_ascii=False)


