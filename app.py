from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World Flask!"

if __name__ == '__main__':
    app.run(host='localhost', port=6000)