from flask import Flask
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index-en.html')


if __name__ == '__main__':
    app.run()
