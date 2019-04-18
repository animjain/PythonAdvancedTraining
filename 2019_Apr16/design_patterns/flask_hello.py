from flask import Flask

app = Flask("myapp")

@app.route("/")
def hello():
    return "<h1>Hello world</h1>"

@app.route("/about")
def about():
    return "<h1>About me...</h1>"

if __name__ == '__main__':
    app.run()
