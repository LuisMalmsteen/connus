from flask import Flask, jsonify
from flask import make_response

from controller.CSVJoiner import CSVJoiner

app = Flask(__name__)


@app.route('/taskConfig/', methods=['POST'])
def task_config():
    #main_process = MainProcessController()
    #alarms = main_process.getAlarmsJSON()
    csv = CSVJoiner()
    print(csv.joinReport({}))

    return make_response(jsonify({'code': 1, 'result': True, 'message': "OK"}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010, debug=False)
