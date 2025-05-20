from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/hello")
def hello():
    return "Hello there buddy"

if __name__ == "__main__":
    app.run(port = 8080, host = "0.0.0.0")