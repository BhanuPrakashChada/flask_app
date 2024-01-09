# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Flask App'
    heading = 'Welcome to Flask App!'
    info = 'This is a simple Flask application which will run inside a Docker container.'

    return render_template('index.html', title=title, heading=heading, info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
