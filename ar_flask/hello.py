from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route("/username/<name>")
def sveiciens(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)