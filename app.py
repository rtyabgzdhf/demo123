from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! abz sdskd test 5678 at ' + str(datetime.datetime.now())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

