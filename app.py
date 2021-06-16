from flask import Flask, g, request

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    app.run()