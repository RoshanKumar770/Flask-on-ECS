from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask on Docker!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to Flask on Docker.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
