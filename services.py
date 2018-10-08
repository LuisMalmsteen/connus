from flask import Flask
from controller.ServiceControllers import MyClass

app = Flask(__name__)


@app.route('/bigReveal', methods=['GET'])
def big_reveal():
    services = MyClass()

    return "Big reveal, i'm mathing: " + str(services.sum(3, 4))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010, debug=False)
