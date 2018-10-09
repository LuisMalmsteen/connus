import requests


class MainProcessController:

    def get_zoho_token(self):
        str_req = 'https://accounts.zoho.com/apiauthtoken/nb/create?SCOPE=ZohoReports/' \
                  'reportsapi&EMAIL_ID=luis@connus.mx&PASSWORD=Psylocke!1'
        return requests.post(str_req)

    def getAlarmsJSON(self):
        auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1YTg0ODMwMjQ3ZjBhZ' \
                     'TEwZTkwMDNkZDciLCJhY2MiOjQsImNtcCI6IjVhMDA3Yzk2YjhhNWU4NDM1ZmQ5MGVhY' \
                     'SIsImlhdCI6MTUzMDY1MDAyNH0.r4qLHckl_Lw7HG3ZHipqm05hOVwLDeZLVjkZUi0mjzI'

        headers = {'Authorization': 'Bearer ' + auth_token, 'content-type': "application/json"}

        return requests.get('http://localhost:8080/v1/reports/alarmsByJson', headers=headers).json()


