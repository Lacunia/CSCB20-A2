from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Welcome, user, to my CSCB20 website!</h1>'

@app.route('/<name>')
def user(name):
    name = name.strip()
    name = name.swapcase()
    return '<h1>Welcome, {}, to my CSCB20 website!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)